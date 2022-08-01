import random
import transformers
import torch
import torch.nn as nn
from transformers.models.bert.modeling_bert import BertModel
from transformers import BertTokenizer
import glob
import importlib
import os
import sys
from pathlib import Path

config = transformers.BertConfig()
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")


class BERT_TOP(nn.Module):
    def __init__(self):
        super(BERT_TOP, self).__init__()
        self.bert = BertModel(config)

    def forward(self, inputs):
        x = self.bert(**inputs)
        return x



class CLASSIFIER_BOTTOM(nn.Module):
    def __init__(self, names_ouput):
        super(CLASSIFIER_BOTTOM, self).__init__()
        self.bert_drop = nn.Dropout(0.4)
        self.out = nn.Linear(768, names_ouput["output_size"])

    def forward(self, pooledOut):
        bertOut = self.bert_drop(pooledOut)
        output = self.out(bertOut)
        return output


def get_bool_result(value, **keywords):
    number = value.argmax(1).item()
    return [True, False][number]


def get_bool_loss(results_network, answers, **keywords):
    loss_fn = nn.CrossEntropyLoss()
    value = [0] * keywords["output_size"]
    value[int(answers)] = 1
    value = torch.tensor([value])
    test_loss = loss_fn(results_network, value).item()
    return test_loss


def get_classes_result(value, values=[], **keywords):
    number = value.argmax(1).item()

    return values[number]


def get_classes_loss(results_network, answers, **keywords):
    loss_fn = nn.CrossEntropyLoss()
    x = [0] * keywords["output_size"]
    x[answers] = 1
    x = torch.tensor([x])
    test_loss = loss_fn(results_network, x).item()
    return test_loss

## load 
module_list = []
def load_modules():
    modules = glob.glob('/home/william/Code/Python/bod/machine_learning/exter_dataset/*.py')
    for module in modules:
        stem = Path(module).stem
        try:
            m = importlib.import_module("."+stem,"machine_learning.exter_dataset")
            module_list.append(m)
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(
                exc_tb.tb_frame.f_code.co_filename)[1]
            print("b:", exc_type, exc_obj,
                  exc_tb, fname, exc_tb.tb_lineno)
            print("error:",stem)



names_ouput = {
    "boolen_factCheck": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },

    "3_lies": {
        "output_size": 3,
        "values": ["False", "true but needs verification", "True"],
        "output": get_classes_result,
        "loss": get_classes_loss,
    },
    "4_factCheck": {
        "output_size": 4,
        "values": ["False", "Mostly false",
                     "Half true", "Mostly true", "True"],
        "output": get_classes_result,
        "loss": get_classes_loss,
    },
    "boolen_sensitive": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_toxicity": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_severe_toxicity": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_obscene": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_threat": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_identity_attack": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_homophobia": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_insult": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_racism": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_xenophobia": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_race": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_profession": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_gender": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_Homophobic": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_Transphobic": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_hate_speech": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_offensive_language": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_Hoax": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_Sarcastic": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_Hate": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_racism": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_offensive": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_sarcasm": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_satire": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_irony": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_overstatement": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_understatement": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_rhetorical question": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_FactClaiming": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_Engaging": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_nominal_utterance": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_news": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_stereotype": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_irony": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_offensiveness": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_aggressiveness": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "boolen_hate_speech": {
        "output_size": 2,
        "output": get_bool_result,
        "loss": get_bool_loss,
    },
    "3_Class of Hate": {
        "output_size": 3,
        "values": ["A", "B", "C"],
        "output": get_classes_result,
        "loss": get_classes_loss,
    }
}


class classify_brain(nn.Module):
    def __init__(self):
        super(classify_brain, self).__init__()
        self.outputs = {}
        self.bert_top = BERT_TOP()
        for name_ouput in names_ouput.keys():
            self.outputs[name_ouput] = CLASSIFIER_BOTTOM(
                names_ouput[name_ouput])

    def forward(self, inputs, output_need=None):
        output = {}
        x = self.bert_top(inputs)
        if output_need is None:
            for output_key in self.outputs.keys():
                output[output_key] = self.outputs[output_key](x.pooler_output)
        else:
            for output_key in output_need:
                output[output_key] = self.outputs[output_key](x.pooler_output)
        return output


top = classify_brain()


def train(inputs):
    x = top(inputs)
    for name in x.keys():
        cccs = names_ouput[name]['output'](x[name], **names_ouput[name])
        names_ouput[name]["loss"]



def main ():
    load_modules()
    inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
    while True:
        train(inputs)
        break
main()