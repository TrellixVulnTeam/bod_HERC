url = "https://github.com/firojalam/COVID-19-disinformation"
import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'COVID-19-disinformation',url)



def get_data():
    # arabic
    covid19_disinfo_arabic_binary_dev = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_binary_dev.tsv")
    covid19_disinfo_arabic_binary_test = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_binary_test.tsv")
    covid19_disinfo_arabic_binary_train = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_binary_train.tsv")
    covid19_disinfo_arabic_multiclass_dev = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_multiclass_dev.tsv")
    covid19_disinfo_arabic_multiclass_test = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_multiclass_test.tsv")
    covid19_disinfo_arabic_multiclass_train = get_path(dir_fs, 'COVID-19-disinformation',"data/arabic/covid19_disinfo_arabic_multiclass_train.tsv")
    # bulgarian
    covid19_disinfo_bulgarian_binary_dev = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_binary_dev.tsv")
    covid19_disinfo_bulgarian_binary_test = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_binary_test.tsv")
    covid19_disinfo_bulgarian_binary_train = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_binary_train.tsv")
    covid19_disinfo_bulgarian_multiclass_dev = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_multiclass_dev.tsv")
    covid19_disinfo_bulgarian_multiclass_test = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_multiclass_test.tsv")
    covid19_disinfo_bulgarian_multiclass_train = get_path(dir_fs, 'COVID-19-disinformation',"data/bulgarian/covid19_disinfo_bulgarian_multiclass_train.tsv")
    # dutch
    covid19_disinfo_dutch_binary_dev = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_binary_dev.tsv")
    covid19_disinfo_dutch_binary_test = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_binary_test.tsv")
    covid19_disinfo_dutch_binary_train = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_binary_train.tsv")
    covid19_disinfo_dutch_multiclass_dev = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_multiclass_dev.tsv")
    covid19_disinfo_dutch_multiclass_test = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_multiclass_test.tsv")
    covid19_disinfo_dutch_multiclass_train = get_path(dir_fs, 'COVID-19-disinformation',"data/dutch/covid19_disinfo_dutch_multiclass_train.tsv")
    # english
    covid19_disinfo_english_binary_dev = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_binary_dev.tsv")
    covid19_disinfo_english_binary_test = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_binary_test.tsv")
    covid19_disinfo_english_binary_train = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_binary_train.tsv")
    covid19_disinfo_english_multiclass_dev = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_multiclass_dev.tsv")
    covid19_disinfo_english_multiclass_test = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_multiclass_test.tsv")
    covid19_disinfo_english_multiclass_train = get_path(dir_fs, 'COVID-19-disinformation',"data/english/covid19_disinfo_english_multiclass_train.tsv")
    # multilang
    covid19_disinfo_multilang_binary_dev = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_binary_dev.tsv")
    covid19_disinfo_multilang_binary_test = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_binary_test.tsv")
    covid19_disinfo_multilang_binary_train = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_binary_train.tsv")
    covid19_disinfo_multilang_multiclass_dev = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_multiclass_dev.tsv")
    covid19_disinfo_multilang_multiclass_test = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_multiclass_test.tsv")
    covid19_disinfo_multilang_multiclass_train = get_path(dir_fs, 'COVID-19-disinformation',"data/multilang/covid19_disinfo_multilang_multiclass_train.tsv")
