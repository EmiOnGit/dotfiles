#!/bin/python

import glob
import sys
import subprocess
import json
from pathlib import Path

if sys.argv:
    path = sys.argv[1]
else:
    path = "~"

path = path.replace("~", str(Path.home()))
path = path.replace("$HOME", str(Path.home()))
if path[-2:] != "/*":
    path += "/*"

children_paths=glob.glob(path) 
children_names=[child.split("/")[-1].upper() for child in children_paths]

children = list(zip(children_names, children_paths))
json_str=json.dumps(children)
subprocess.run(['eww', 'update', str('FOLDER=' + json_str)])
