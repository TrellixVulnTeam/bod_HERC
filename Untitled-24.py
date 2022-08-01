import glob
import importlib
from pathlib import Path
from sqlite3 import paramstyle
from urllib.error import HTTPError
from wsgiref.simple_server import WSGIRequestHandler
from alive_progress import alive_bar
no_errors = []
errors = []
modules = glob.glob('/home/william/Code/Python/bod/machine_learning/exter_dataset/*.py')
count = len(modules)
for module in modules:
    if "PUBHEALTH" not in module:
        continue
    stem = Path(module).stem
    a = importlib.import_module("."+stem,"machine_learning.exter_dataset")


while True:
    x = getattr(a,"get_data")
    print(x())