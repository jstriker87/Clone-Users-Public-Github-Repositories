import requests
import os
import argparse
from pathlib import Path
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    "--maxrepos", "--mr", help="Set the maximum number of repos to clone", type=int
)

parser.add_argument(
    "--username", "--u", help="Set username of Git repo to use", type=str
)

parser.add_argument(
    "--file", "-f", help="Set input Excel file to use", type=str
)

args = parser.parse_args()
maxrepos = args.maxrepos if args.maxrepos else 5

if not args.file and not args.username:
        raise Exception("error: the following arguments are required: --username")

file_lists = dict()
if args.file:
    if not "xls" in args.file:
        raise Exception("File is not an Excel file") 

    df = pd.read_excel(args.file)
    for index, row in df.iterrows():
        file_lists[row['Name']] = row['Username']


if len(file_lists) == 0:
    url = f"https://api.github.com/users/{args.username}/repos?sort=updated&direction=desc"
    response = requests.get(url)
    response = response.json()
    Path(os.path.dirname(os.path.abspath(__file__)) + "/" + args.username).mkdir(parents=True, exist_ok=True)
    os.chdir( os.path.dirname(os.path.abspath(__file__)) + "/" + args.username)
    i = 1
    for item in response:
        if i > maxrepos:
            break
        os.system("git clone " + item["clone_url"])
        i = i + 1

else:
    for key, value in file_lists.items():

        url = f"https://api.github.com/users/{value}/repos?sort=updated&direction=desc"
        response = requests.get(url)
        response = response.json()
        folderPath = key + '-' + value
        Path(os.path.dirname(os.path.abspath(__file__)) + "/" + folderPath).mkdir(parents=True, exist_ok=True)
        os.chdir( os.path.dirname(os.path.abspath(__file__)) + "/" + folderPath)
        i = 1
        for item in response:
            if i > maxrepos:
                break
            os.system("git clone " + item["clone_url"])
            i+=1
