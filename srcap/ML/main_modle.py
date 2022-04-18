# from transformers import BartForConditionalGeneration, BartTokenizer

# model = BartForConditionalGeneration.from_pretrained(
#     "facebook/bart-large", forced_bos_token_id=0)
# tok = BartTokenizer.from_pretrained("facebook/bart-large")
# example_english_phrase = "UN Chief Says There Is No <mask> in Syria"
# batch = tok(example_english_phrase, return_tensors="pt")
