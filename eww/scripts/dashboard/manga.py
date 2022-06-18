import subprocess
import json
from pathlib import Path
import sys

manga_name = "One Piece"
manga_provider = "8"
mangal_path = Path.home().joinpath(".config/mangal/")
manga_name = "\"" + manga_name + "\""

def has_new_episode():
    with open(mangal_path.joinpath("current.json")) as f:
        data = json.load(f)
        command = ['mangal', 'inline', 
        '--query', manga_name, 
        "--manga", manga_provider, 
        "--json"]
        out = subprocess.run(' '.join(command), shell=True, capture_output=True).stdout
        data2 = json.loads(out)
        current_in_db = data2[len(data2) - 1]["index"]
        return data["current"] != current_in_db

def open_latest_episode():
    write_latest_episode()
    command = ['mangal', 'inline', 
    '--query', manga_name, 
    "--manga", manga_provider, 
    "--chapter", "1",
    "--read"]
    subprocess.run(' '.join(command), shell=True, capture_output=True).stdout
    

def write_latest_episode():
    with open(mangal_path.joinpath("current.json"), "r") as f:
        bookmark = json.load(f)
    command = ['mangal', 'inline', 
    '--query', manga_name, 
    "--manga", manga_provider, 
    "--json"]
    out = subprocess.run(' '.join(command), shell=True, capture_output=True).stdout
    database_data = json.loads(out)
    current_in_db = database_data[len(database_data) - 1]["index"]
    bookmark["current"] = current_in_db
    with open(mangal_path.joinpath("current.json"), "w") as f:
        json.dump(bookmark, f)


        
if len(sys.argv) > 1:
    if sys.argv[1] == "read":
        print("hi")
        open_latest_episode()
    if sys.argv[1] == "update":
        print(has_new_episode())
