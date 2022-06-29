import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/mayelsherif/hate_speech_icwsm18"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hate_speech_icwsm18',url)


def get_data():
    paths = [
    "twitter_key_phrase_based_datasets/archaic_boojie.csv",
    "twitter_key_phrase_based_datasets/archaic_chinaman.csv",
    "twitter_key_phrase_based_datasets/archaic_hillbilly.csv",
    "twitter_key_phrase_based_datasets/archaic_surrendermonkey.csv",
    "twitter_key_phrase_based_datasets/archaic_whigger.csv",
    "twitter_key_phrase_based_datasets/archaic_wigerette.csv",
    "twitter_key_phrase_based_datasets/archaic_wigger.csv",
    "twitter_key_phrase_based_datasets/class_bitterclinger.csv",
    "twitter_key_phrase_based_datasets/class_conspiracytheorist.csv",
    "twitter_key_phrase_based_datasets/class_redneck.csv",
    "twitter_key_phrase_based_datasets/class_rube.csv",
    "twitter_key_phrase_based_datasets/class_trailerparktrash.csv",
    "twitter_key_phrase_based_datasets/class_whitetrash.csv",
    "twitter_key_phrase_based_datasets/disability_retard.csv",
    "twitter_key_phrase_based_datasets/disability_retarded.csv",
    "twitter_key_phrase_based_datasets/ethn_camelfucker.csv",
    "twitter_key_phrase_based_datasets/ethn_coonass.csv",
    "twitter_key_phrase_based_datasets/ethn_housenigger.csv",
    "twitter_key_phrase_based_datasets/ethn_mooncricket.csv",
    "twitter_key_phrase_based_datasets/ethn_nigger.csv",
    "twitter_key_phrase_based_datasets/ethn_raghead.csv",
    "twitter_key_phrase_based_datasets/ethn_spic.csv",
    "twitter_key_phrase_based_datasets/ethn_trailerparktrash.csv",
    "twitter_key_phrase_based_datasets/ethn_trailertrash.csv",
    "twitter_key_phrase_based_datasets/ethn_wetback.csv",
    "twitter_key_phrase_based_datasets/ethn_whitenigger.csv",
    "twitter_key_phrase_based_datasets/ethn_whitetrash.csv",
    "twitter_key_phrase_based_datasets/gender_bint.csv",
    "twitter_key_phrase_based_datasets/gender_cunt.csv",
    "twitter_key_phrase_based_datasets/gender_dyke.csv",
    "twitter_key_phrase_based_datasets/gender_twat.csv",
    "twitter_key_phrase_based_datasets/nation_bamboocoon.csv",
    "twitter_key_phrase_based_datasets/nation_camelfucker.csv",
    "twitter_key_phrase_based_datasets/nation_chinaman.csv",
    "twitter_key_phrase_based_datasets/nation_limey.csv",
    "twitter_key_phrase_based_datasets/nation_plasticpaddy.csv",
    "twitter_key_phrase_based_datasets/nation_sidewayspussy.csv",
    "twitter_key_phrase_based_datasets/nation_surrendermonkey.csv",
    "twitter_key_phrase_based_datasets/nation_whigger.csv",
    "twitter_key_phrase_based_datasets/nation_whitenigger.csv",
    "twitter_key_phrase_based_datasets/nation_wigger.csv",
    "twitter_key_phrase_based_datasets/nation_zionazi.csv",
    "twitter_key_phrase_based_datasets/rel_camelfucker.csv",
    "twitter_key_phrase_based_datasets/rel_muzzie.csv",
    "twitter_key_phrase_based_datasets/rel_souptaker.csv",
    "twitter_key_phrase_based_datasets/rel_zionazi.csv",
    "twitter_key_phrase_based_datasets/sexorient_dyke.csv",
    "twitter_key_phrase_based_datasets/sexorient_faggot.csv",
    "twitter_hashtag_based_datasets/ethn_blackpeoplesuck.csv",
    "twitter_hashtag_based_datasets/ethn_whitepower.csv",
    "twitter_hashtag_based_datasets/istandwithhatespeech.csv",
    "twitter_hashtag_based_datasets/rel_nomuslimrefugees.csv"
    ]
    path = random.choice(paths)
    if "archaic_boojie" in path:
        pass
    elif "archaic_chinaman" in path:
        pass
    elif "archaic_hillbilly" in path:
        pass
    elif "archaic_surrendermonkey" in path:
        pass
    elif "archaic_whigger" in path:
        pass
    elif "archaic_wigerette" in path:
        pass
    elif "archaic_wigger" in path:
        pass
    elif "class_bitterclinger" in path:
        pass
    elif "class_conspiracytheorist" in path:
        pass
    elif "class_redneck" in path:
        pass
    elif "class_rube" in path:
        pass
    elif "class_trailerparktrash" in path:
        pass
    elif "class_whitetrash" in path:
        pass
    elif "disability_retard" in path:
        pass
    elif "disability_retarded" in path:
        pass
    elif "ethn_camelfucker" in path:
        pass
    elif "ethn_coonass" in path:
        pass
    elif "ethn_housenigger" in path:
        pass
    elif "ethn_mooncricket" in path:
        pass
    elif "ethn_nigger" in path:
        pass
    elif "ethn_raghead" in path:
        pass
    elif "ethn_spic" in path:
        pass
    elif "ethn_trailerparktrash" in path:
        pass
    elif "ethn_trailertrash" in path:
        pass
    elif "ethn_wetback" in path:
        pass
    elif "ethn_whitenigger" in path:
        pass
    elif "ethn_whitetrash" in path:
        pass
    elif "gender_bint" in path:
        pass
    elif "gender_cunt" in path:
        pass
    elif "gender_dyke" in path:
        pass
    elif "gender_twat" in path:
        pass
    elif "nation_bamboocoon" in path:
        pass
    elif "nation_camelfucker" in path:
        pass
    elif "nation_chinaman" in path:
        pass
    elif "nation_limey" in path:
        pass
    elif "nation_plasticpaddy" in path:
        pass
    elif "nation_sidewayspussy" in path:
        pass
    elif "nation_surrendermonkey" in path:
        pass
    elif "nation_whigger" in path:
        pass
    elif "nation_whitenigger" in path:
        pass
    elif "nation_wigger" in path:
        pass
    elif "nation_zionazi" in path:
        pass
    elif "rel_camelfucker" in path:
        pass
    elif "rel_muzzie" in path:
        pass
    elif "rel_souptaker" in path:
        pass
    elif "rel_zionazi" in path:
        pass
    elif "sexorient_dyke" in path:
        pass
    elif "sexorient_faggot" in path:
        pass
    elif "ethn_blackpeoplesuck" in path:
        pass
    elif "ethn_whitepower" in path:
        pass
    elif "istandwithhatespeech" in path:
        pass
    elif "rel_nomuslimrefugees" in path:
        pass