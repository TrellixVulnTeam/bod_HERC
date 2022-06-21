from machine_learning.service_scrap.transformer.compressive_transformers.compressive_transformer_pytorch import default


class SelfAttention(nn.Module):
    def __init__(self,  dim, depth, max_seq_len, heads, local_attn_heads, window_size, dim_head = None, local_attn_window_size = None, local_attn_radius_blocks = 1, causal = False, attn_dropout = 0., dropout = 0., kmeans_ema_decay = 0.999, commitment_factor = 1e-4, receives_context = False, context_window_size = None, rel_pos_emb = True, num_mem_kv = 0, shared_qk = False, conv_query_kernel = 9):
        super().__init__()
        assert dim_head or (dim % heads) == 0, 'hidden dimension must be divisible by number of heads'
        assert (max_seq_len % window_size) == 0, 'maximum sequence length must be divisible by the target window size'
        assert local_attn_heads <= heads, 'number of local attention heads must be less than total heads'
        assert not (receives_context and local_attn_heads > 0), 'local attention cannot be used for self attention with context'
        assert not (receives_context and causal), 'contextual attention layer cannot be causal'

        local_attn_window_size = default(local_attn_window_size, window_size)
        context_window_size = default(context_window_size, window_size)

        self.shared_qk = shared_qk
        self.receives_context = receives_context
        self.heads = heads
        self.local_attn_heads = local_attn_heads
        self.global_attn_heads = heads - local_attn_heads

        self.causal = causal
        self.window_size = window_size

        dim_head = default(dim_head, dim // heads)
        dim_heads = dim_head * heads
        self.dim_head = dim_head

        num_clusters = max_seq_len // window_size

        # local

        local_dim_heads = dim_head * self.local_attn_heads

        if self.local_attn_heads > 0:
            rel_pos_emb_config = (dim_head, local_attn_heads) if rel_pos_emb else None
            self.local_attn = LocalAttention(dim = dim_head, window_size = local_attn_window_size, causal = causal, dropout = attn_dropout, rel_pos_emb_config = rel_pos_emb_config, look_backward = local_attn_radius_blocks, look_forward = 0 if causal else local_attn_radius_blocks)
            self.local_to_qkv = nn.Linear(dim, 3 * local_dim_heads)

        # global

        global_dim_heads = dim_head * self.global_attn_heads

        if self.global_attn_heads > 0:
            self.global_attn = KmeansAttention(num_clusters, window_size, self.global_attn_heads, dim_head, causal = causal, dropout = attn_dropout, ema_decay = kmeans_ema_decay, commitment = commitment_factor, receives_context = receives_context, num_mem_kv = num_mem_kv, shared_qk = shared_qk)

        self.to_q = nn.Linear(dim, global_dim_heads, bias = False)
        self.to_v = nn.Linear(dim, global_dim_heads, bias = False)

        if not self.shared_qk:
            self.to_k = nn.Linear(dim, global_dim_heads, bias = False)

        # out

        self.to_out = nn.Linear(dim_heads, dim, bias = False)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, context = None, input_mask = None, context_mask = None, pos_emb = None, **kwargs):
        assert not (self.receives_context and not exists(context)), 'context must be passed if self attention is set to receive context'
        b, t, e, h, dh = *x.shape, self.heads, self.dim_head
        has_local, has_global = map(lambda x: x > 0, (self.local_attn_heads, self.global_attn_heads))

        split_heads = lambda v: reshape_dim(v, -1, (-1, dh)).transpose(1, 2).contiguous()

        if has_local:
            local_qkv = self.local_to_qkv(x).chunk(3, dim=-1)
            lq, lk, lv = map(split_heads, local_qkv)

        if has_global:
            kv_input = x if not self.receives_context else context

            q, v = self.to_q(x), self.to_v(kv_input)

            if not self.shared_qk:
                k = self.to_k(kv_input)
            else:
                k = self.to_q(kv_input) if self.receives_context else q

            q, k, v = map(split_heads, (q, k, v))

        out = []
        total_loss = torch.tensor(0., requires_grad=True, **to(x))

        if has_local:
            local_out = self.local_attn(lq, lk, lv, input_mask = input_mask)
            out.append(local_out)

        if has_global:
            if not self.receives_context and exists(pos_emb):
                q, k, v = apply_rotary_pos_emb(q, k, v, pos_emb)

            global_out, loss = self.global_attn(q, k, v, query_mask = input_mask, key_mask = context_mask)
            total_loss = total_loss + loss

            out.append(global_out)

        out = torch.cat(out, dim=1)
        out = out.reshape(b, h, t, -1).transpose(1, 2).reshape(b, t, -1)
        out = self.to_out(out)
        return self.dropout(out), total_loss