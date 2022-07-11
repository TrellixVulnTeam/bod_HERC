import glob
import importlib
from pathlib import Path
import sys
import os
from tqdm import tqdm

modules = glob.glob('/home/william/Code/Python/bod/machine_learning/exter_dataset/*.py')
for module in tqdm(modules):
    stem = Path(module).stem
    try:
        importlib.import_module("."+stem,"machine_learning.exter_dataset")
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(
            exc_tb.tb_frame.f_code.co_filename)[1]
        print("b:", exc_type, exc_obj,
              exc_tb, fname, exc_tb.tb_lineno)
        print("error:",stem)