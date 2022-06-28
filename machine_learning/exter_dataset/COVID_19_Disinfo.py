import os
import random
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/firojalam/COVID-19-disinformation"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'COVID_19_Disinfo',url)


def get_data():
    if random.choice([True,False]):
        covid19_disinfo_english_binary_dev = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_binary_dev.tsv")
        covid19_disinfo_english_binary_test = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_binary_test.tsv")
        covid19_disinfo_english_binary_train = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_binary_train.tsv")
        path = random.choice([covid19_disinfo_english_binary_dev,covid19_disinfo_english_binary_test,covid19_disinfo_english_binary_train])
        data = None
        data["tweet_id"]
        data["q1_label"]
        data["q2_label"]
        data["q3_label"]
        data["q4_label"]
        data["q5_label"]
        data["q6_label"]
        data["q7_label"]

    else:
        covid19_disinfo_english_multiclass_dev = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_multiclass_dev.tsv")
        covid19_disinfo_english_multiclass_test = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_multiclass_test.tsv")
        covid19_disinfo_english_multiclass_train = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_multiclass_train.tsv")
        path = random.choice([covid19_disinfo_english_multiclass_dev,covid19_disinfo_english_multiclass_test,covid19_disinfo_english_multiclass_train])
        data = None
        data["tweet_id"]
        # no
        # yes
        if data["q1_label"] == "no":
            pass
        elif data["q1_label"] == "yes":
            pass
        # NA
        # 1_no_definitely_contains_no_false_info
        # 2_no_probably_contains_no_false_info
        # 3_not_sure
        # 4_yes_probably_of_interest
        # 5_yes_definitely_of_interest
        if data["q2_label"] == "1_no_definitely_contains_no_false_info":
            pass
        elif data["q2_label"] == "2_no_probably_contains_no_false_info":
            pass
        elif data["q2_label"] == "3_not_sure":
            pass
        elif data["q2_label"] == "4_yes_probably_of_interest":
            pass
        elif data["q2_label"] == "5_yes_definitely_of_interest":
            pass
        # NA
        # 1_no_definitely_not_harmful
        # 2_no_probably_not_harmful
        # 3_not_sure
        # 4_yes_probably_harmful
        # 5_yes_definitely_harmful

        if data["q3_label"] == "1_no_definitely_not_harmful":
            pass
        elif data["q3_label"] == "2_no_probably_not_harmful":
            pass
        elif data["q3_label"] == "3_not_sure":
            pass
        elif data["q3_label"] == "4_yes_probably_harmful":
            pass
        elif data["q3_label"] == "5_yes_definitely_harmful":
            pass
        # NA
        # 1_no_definitely_not_harmful
        # 2_no_probably_not_harmful
        # 3_not_sure
        # 4_yes_probably_harmful
        # 5_yes_definitely_harmful
        if data["q4_label"] == "1_no_definitely_not_harmful":
            pass
        elif data["q4_label"] == "2_no_probably_not_harmful":
            pass
        elif data["q4_label"] == "3_not_sure":
            pass
        elif data["q4_label"] == "4_yes_probably_harmful":
            pass
        elif data["q4_label"] == "5_yes_definitely_harmful":
            pass
        # NA
        # no_no_need_to_check
        # no_too_trivial_to_check
        # not_sure
        # yes_not_urgent
        # yes_very_urgent
        if data["q5_label"] == "":
            pass
        # # no_joke_or_sarcasm
        # no_not_harmful
        # not_sure
        # yes_bad_cure
        # yes_other
        # yes_panic
        # yes_rumor_conspiracy
        # yes_xenophobic_racist_prejudices_or_hate_speech

        if data["q6_label"] == "":
            pass
        # yes_other
        # yes_discusses_cure
        # yes_discusses_action_taken
        # yes_contains_advice
        # yes_classified_as_in_question_6
        # yes_calls_for_action
        # yes_blame_authorities
        # yes_asks_question
        # not_sure
        # no_not_interesting
        if data["q7_label"] == "":
            pass
        elif data["q7_label"] == "":
            pass
        elif data["q7_label"] == "":
            pass
        elif data["q7_label"] == "":
            pass
        elif data["q7_label"] == "":
            pass
        elif data["q7_label"] == "":
            pass
        elif data["q7_label"] == "":
            pass

 