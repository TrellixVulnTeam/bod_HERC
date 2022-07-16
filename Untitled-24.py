import glob
import importlib
import json
from pathlib import Path
from sqlite3 import paramstyle
import sys
import os
import time
import urllib
from urllib.error import HTTPError
from alive_progress import alive_bar
no_errors = []
errors = []
modules = glob.glob('/home/william/Code/Python/bod/machine_learning/exter_dataset/*.py')
count = len(modules)
with alive_bar(count) as bar:
    for module in modules:
        start_start = time.time_ns()
        stem = Path(module).stem
        try:
            a = importlib.import_module("."+stem,"machine_learning.exter_dataset")
            for i in range(20):
                start_start2= time.time_ns()
                try:
                    start_end2= time.time_ns()
                    x = a.get_data()
                    if x is None:
                        errors.append(("get_data_return_none",module,start_end2-start_start2,i))
                    else:
                        no_errors.append(("get_data_safe",module,"","","",start_end2-start_start2,i))
                except:
                    start_start2= time.time_ns()
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    errors.append(("get_data_error",module,exc_type, fname, exc_tb.tb_lineno,start_end2-start_start2,str(e)))
            start_end = time.time_ns()
            no_errors.append(("loader",module,start_end-start_start))
            print(module)
        except HTTPError as e:
            
            start_end = time.time_ns()
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors.append(("get_data",module,exc_type, fname, exc_tb.tb_lineno,start_end-start_start,str(e)))
            pass
        except:
            
            start_end = time.time_ns()
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors.append(("error loader",module,exc_type, fname, exc_tb.tb_lineno,start_end-start_start))
        bar()

def Errors_time(e):
      return e[5]

  
os.system('clear')
print("ERROR")
errors.sort(key=Errors_time)
for error in errors:
    print(error)


def noErrors_time(e):
      return e[2]
no_errors.sort(key=noErrors_time)
print("NO ERROR")
for no_error in no_errors:
    print(no_error)



data = json.dumps({"no_error":no_error,"error":error})
with  open("results.text","w") as file:
    file.write(data)
file.close()