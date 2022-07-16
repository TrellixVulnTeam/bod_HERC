from difflib import SequenceMatcher
import time
import torch
import torch.nn as nn
from alive_progress import alive_bar

filter_ratio = 1


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


text = """
        Another one got caught today, it's all over the papers.  "Teenager
Arrested in Computer Crime Scandal", "Hacker Arrested after Bank Tampering"...
        Damn kids.  They're all alike.

        But did you, in your three-piece psychology and 1950's technobrain,
ever take a look behind the eyes of the hacker?  Did you ever wonder what
made him tick, what forces shaped him, what may have molded him?
        I am a hacker, enter my world...
        Mine is a world that begins with school... I'm smarter than most of
the other kids, this crap they teach us bores me...
        Damn underachiever.  They're all alike.

        I'm in junior high or high school.  I've listened to teachers explain
for the fifteenth time how to reduce a fraction.  I understand it.  "No, Ms.
Smith, I didn't show my work.  I did it in my head..."
        Damn kid.  Probably copied it.  They're all alike.

        I made a discovery today.  I found a computer.  Wait a second, this is
cool.  It does what I want it to.  If it makes a mistake, it's because I
screwed it up.  Not because it doesn't like me...
                Or feels threatened by me...
                Or thinks I'm a smart ass...
                Or doesn't like teaching and shouldn't be here...
        Damn kid.  All he does is play games.  They're all alike.

        And then it happened... a door opened to a world... rushing through
the phone line like heroin through an addict's veins, an electronic pulse is
sent out, a refuge from the day-to-day incompetencies is sought... a board is
found.
        "This is it... this is where I belong..."
        I know everyone here... even if I've never met them, never talked to
them, may never hear from them again... I know you all...
        Damn kid.  Tying up the phone line again.  They're all alike...

        You bet your ass we're all alike... we've been spoon-fed baby food at
school when we hungered for steak... the bits of meat that you did let slip
through were pre-chewed and tasteless.  We've been dominated by sadists, or
ignored by the apathetic.  The few that had something to teach found us will-
ing pupils, but those few are like drops of water in the desert.

        This is our world now... the world of the electron and the switch, the
beauty of the baud.  We make use of a service already existing without paying
for what could be dirt-cheap if it wasn't run by profiteering gluttons, and
you call us criminals.  We explore... and you call us criminals.  We seek
after knowledge... and you call us criminals.  We exist without skin color,
without nationality, without religious bias... and you call us criminals.
You build atomic bombs, you wage wars, you murder, cheat, and lie to us
and try to make us believe it's for our own good, yet we're the criminals.

        Yes, I am a criminal.  My crime is that of curiosity.  My crime is
that of judging people by what they say and think, not what they look like.
My crime is that of outsmarting you, something that you will never forgive me
for.

        I am a hacker, and this is my manifesto.  You may stop this individual,
but you can't stop us all... after all, we're all alike.
"""


def split(str, length):
    if length != 0:
        for c in range(0, len(str)-length, 1):
            yield str[c:c+length]





def sort_fitness(d):
    return d["fitness"]

def sort_frequency(d):
    return d["frequency"]

def sort_length(d):
    return d["length"]



text_byte = bytes(text, 'UTF-8')
index = 0
best_chunk = []


def finder_awnser(index, chunk_list, data):
    for chunk in chunk_list:
        end_at = index+chunk["length"]
        if end_at < len(data):
            if data[index:end_at] == chunk["chunk"]:
                return True, index+chunk["length"], chunk
    return False, index, ""


def chunkList(chunk_list,chunk):
    in_chunk = True
    if chunk in chunk_list:
        in_chunk = False
    return in_chunk

def fit(chunk,frequency):
    return (len(chunk))*frequency


class UpperTokenizer(nn.Module):
    def __init__(self) :
        super().__init__()
        self.chunk_lang = {}
        self.chunk_type = {}
        
        self.index_lang = {}
        self.index_type = {}
        
    def mini_train(self,chunk_list,chunk_list2):
        index = 0
        while index < len(text_byte):
            check, index, chunk = finder_awnser(index, chunk_list, text_byte)
            if check:
                in_chunk = chunkList(chunk_list2,chunk)
                if in_chunk:
                    chunk["frequency"] = 1
                    chunk_list2.append(chunk)
                else:
                    for chunkvvv in chunk_list:
                        if chunk == chunkvvv:
                            chunk["frequency"] = 1 + chunk["frequency"]
                
                chunk["frequency"] = (len(chunk["chunk"])**1.5)*chunk["frequency"]
                continue
            else:
                index = index + 1
        chunk_list2.sort(key=sort_fitness, reverse=False)
        to_remove = []
        for  chunk in (chunk_list2):
            if chunk["frequency"]  == 1:
                to_remove.append(chunk)
        for rm in to_remove:
            chunk_list2.remove(rm)
        if len(chunk_list2) > 60:
            chunk_list2 = chunk_list2[60:]
        return chunk_list2
            
    def train(self,byte_text,lang,type_):
        chunk_dict = {}
        chunk_list = []
        # get frequency
        for count in range(2,90):
            for g in split(byte_text, count):
                if g in chunk_dict.keys():
                    chunk_dict[g] = 1 + chunk_dict[g]
                else:
                    chunk_dict[g] = 1
        chunk_dict2 = []
        # clean up data
        for chunk in chunk_dict.keys():
            length = len(chunk)
            frequency = length*chunk_dict[chunk]
            data = {
                "chunk": chunk,
                "length": length,
                "frequency": chunk_dict[chunk],
                "fitness": fit(chunk,chunk_dict[chunk]),
            }
            if 1 == data["length"] or data["frequency"] == 1:
                continue
            if 1 == len(chunk):
                chunk_dict2.append(data)
            if 1 == chunk_dict[chunk]:
                continue
            if frequency >= len(chunk):
                chunk_dict2.append(data)
            chunk_list = []
        # 
        for chunkA in chunk_dict2:
            c = True
            for chunkB in chunk_list:
                if 1 == chunkB["length"] or chunkA["length"] == 1:
                    continue
                if chunkB["length"] == 1 or chunkA["length"] == 1:
                    continue
                if chunkA["fitness"] >= chunkB["fitness"] and chunkB["chunk"] in chunkA["chunk"]:
                    chunk_list.remove(chunkB)
                    break
                elif chunkB["chunk"] in chunkA["chunk"]:
                    c = False
                    break
            if c:
                chunk_list.append(chunkA)
        chunk_list.sort(key=sort_length, reverse=False)
        ## DO LAGURAGES
        if lang not in self.chunk_lang:
            self.chunk_lang[lang] = []
        self.chunk_lang[lang] = self.mini_train(chunk_list,self.chunk_lang[lang])
        ## DO TYPE
        if type_ not in self.chunk_type:
            self.chunk_type[type_] = []
        self.chunk_type[type_] = self.mini_train(chunk_list,self.chunk_type[type_])
        
        for chunk in self.chunk_type[type_]:
            chunk["fitness"] = chunk["fitness"] - 1
            if chunk["fitness"]< 0:
                self.chunk_type[type_].remove(chunk)
        for chunk in self.chunk_lang[lang]:
            chunk["fitness"] = chunk["fitness"] - 1
            if chunk["fitness"]< 0:
                self.chunk_type[lang].remove(chunk)


    def forward(self,text,lang,type_):
        tokens = []
        byte_text = bytes(text, 'UTF-8')
        self.train(byte_text,lang,type_)
        index = 0
        while index < len(byte_text):
            check = True
            for chunk in self.chunk_lang[lang] + self.chunk_type[type_]:
                if byte_text[index:chunk["length"]+index] == chunk["chunk"]:
                    check = False
                    index = chunk["length"] + index
                    if chunk in self.chunk_lang[lang]:
                        b =self.chunk_type[type_].index(chunk)
                        tokens.append(b+256)
                    if chunk in self.chunk_type[type_]:
                        a = self.chunk_type[type_].index(chunk)
                        tokens.append(a+4872+256)
                    break
            if check:
                tokens.append(int(byte_text[index]))
                index = 1 + index
        
        return torch.tensor([tokens])
                

a = UpperTokenizer()
c = a(text,"aa","bb")
print(c)