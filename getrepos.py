import requests
import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument(
    "--maxrepos", "--mr", help="Set the maximum number of repos to clone", type=int
)

parser.add_argument(
    "-username", help="Set username of Git repo to use", type=str, required=True
)

args = parser.parse_args()
maxrepos = args.maxrepos if args.maxrepos else 5

url = f"https://api.github.com/users/{args.username}/repos?sort=updated&direction=desc"
response = requests.get(url)
response = response.json()
Path(os.path.dirname(os.path.abspath(__file__)) + "/" + args.username).mkdir(parents=True, exist_ok=True)
os.chdir( os.path.dirname(os.path.abspath(__file__)) + "/" + args.username)

i = 0
while i < maxrepos:
    for item in response:
        os.system("git clone " + item["clone_url"])
        i+=1

