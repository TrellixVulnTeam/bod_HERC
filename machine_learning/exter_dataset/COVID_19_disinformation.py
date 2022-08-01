url = "https://github.com/firojalam/COVID-19-disinformation"
from ast import Try
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV 
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


from transformers import BertTokenizer

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'COVID-19-disinformation',url)



def get_data():
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    lang = random.choice(["arabic","bulgarian","dutch","english","multilang"])
    is_binary = random.choice([True,False])
    # arabic
    if lang == "arabic":
        if is_binary:
            dev = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_binary_dev.tsv")
            test = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_binary_test.tsv")
            train = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_binary_train.tsv")
        else:
            dev = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_multiclass_dev.tsv")
            test = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_multiclass_test.tsv")
            train = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_multiclass_train.tsv")
    # bulgarian
    if lang == "bulgarian":
        if is_binary:
            dev = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_binary_dev.tsv")
            test = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_binary_test.tsv")
            train = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_binary_train.tsv")
        else:
            dev = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_multiclass_dev.tsv")
            test = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_multiclass_test.tsv")
            train = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_multiclass_train.tsv")
    # dutch
    if lang == "dutch":
        if is_binary:
            dev = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_binary_dev.tsv")
            test = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_binary_test.tsv")
            train = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_binary_train.tsv")
        else:
            dev = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_multiclass_dev.tsv")
            test = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_multiclass_test.tsv")
            train = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_multiclass_train.tsv")
    # english
    if lang == "english":
        if is_binary:
            dev = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_binary_dev.tsv")
            test = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_binary_test.tsv")
            train = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_binary_train.tsv")
        else:
            dev = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_multiclass_dev.tsv")
            test = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_multiclass_test.tsv")
            train = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_multiclass_train.tsv")
    # multilang
    if lang == "multilang":
        if is_binary:
            dev = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_binary_dev.tsv")
            test = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_binary_test.tsv")
            train = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_binary_train.tsv")
        else:
            dev = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_multiclass_dev.tsv")
            test = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_multiclass_test.tsv")
            train = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_multiclass_train.tsv")
    path = random.choice([dev,test,train])
    data = random.choice(CSV(path))
    if is_binary:
        if data["q1_label"] == "yes":
            pass
        elif data["q1_label"] =="no":
            pass
        if data["q2_label"] == "yes":
            pass
        elif data["q2_label"] =="no":
            pass
        if data["q3_label"] == "yes":
            pass
        elif data["q3_label"] =="no":
            pass
        if data["q4_label"] == "yes":
            pass
        elif data["q4_label"] =="no":
            pass
        if data["q5_label"] == "yes":
            pass
        elif data["q5_label"] =="no":
            pass
        if data["q6_label"] == "yes":
            pass
        elif data["q6_label"] =="no":
            pass
        if data["q7_label"] == "yes":
            pass
        elif data["q7_label"] =="no":
            pass
    else:
        if data["q1_label"] == "yes":
            pass
        elif data["q1_label"] =="no":
            pass
        
        if data["q2_label"] == "1_no_definitely_contains_no_false_info":
            pass
        elif data["q2_label"] =="2_no_probably_contains_no_false_info":
            pass
        elif data["q2_label"] =="3_not_sure":
            pass
        elif data["q2_label"] =="4_yes_probably_contains_false_info":
            pass
        elif data["q2_label"] =="5_yes_definitely_contains_false_info":
            pass
        
        
        if data["q3_label"] == "5_yes_definitely_of_interest":
            pass
        elif data["q3_label"] =="4_yes_probably_of_interest":
            pass
        elif data["q3_label"] =="3_not_sure":
            pass
        elif data["q3_label"] =="2_no_probably_not_of_interest":
            pass
        elif data["q3_label"] =="1_no_definitely_not_of_interest":
            pass
        
        if data["q4_label"] == "1_no_definitely_not_harmful":
            pass
        elif data["q4_label"] =="2_no_probably_not_harmful":
            pass
        elif data["q4_label"] =="3_not_sure":
            pass
        elif data["q4_label"] =="4_yes_probably_harmful":
            pass
        elif data["q4_label"] =="5_yes_definitely_harmful":
            pass
        
        if data["q5_label"] == "no_no_need_to_check":
            pass
        elif data["q5_label"] =="no_too_trivial_to_check":
            pass
        elif data["q5_label"] =="yes_not_urgent":
            pass
        elif data["q5_label"] =="yes_very_urgent":
            pass
        
        if data["q6_label"] == "yes_xenophobic_racist_prejudices_or_hate_speech":
            pass
        elif data["q6_label"] =="yes_rumor_conspiracy":
            pass
        elif data["q6_label"] =="yes_panic":
            pass
        elif data["q6_label"] =="yes_other":
            pass
        elif data["q6_label"] =="yes_bad_cure":
            pass
        elif data["q6_label"] =="no_not_harmful":
            pass
        elif data["q6_label"] =="no_joke_or_sarcasm":
            pass
        
        if data["q7_label"] == "yes_other":
            pass
        elif data["q7_label"] =="yes_discusses_cure":
            pass
        elif data["q7_label"] =="yes_discusses_action_taken":
            pass
        elif data["q7_label"] =="yes_contains_advice":
            pass
        elif data["q7_label"] =="yes_classified_as_in_question_6":
            pass
        elif data["q7_label"] =="yes_calls_for_action":
            pass
        elif data["q7_label"] =="yes_asks_question":
            pass
        elif data["q7_label"] =="not_sure":
            pass
        elif data["q7_label"] =="no_not_interesting":
            pass
        