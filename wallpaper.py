import requests
import json
import ctypes
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('subreddit', nargs="?", default="wallpapers", help="Subreddit Name To Find Image From Default Subreddit is r/wallpapers")
p = parser.add_mutually_exclusive_group()
p.add_argument('--hot', action='store_true', help="Get Hot Posts")
p.add_argument('--new', action='store_true', help="Get New Posts")
p.add_argument('--top', action='store_true', help="Get Top Posts")
p.add_argument('--rising', action='store_true', help="Get Rising Posts")
args = parser.parse_args()

filetypes = ["jpg", "png"]

subreddit = args.subreddit

if args.hot:
    url = "https://www.reddit.com/r/" + subreddit + "/hot/.json"
elif args.new:
    url = "https://www.reddit.com/r/" + subreddit + "/new/.json"
elif args.top:
    url = "https://www.reddit.com/r/" + subreddit + "/top/.json"
elif args.rising:
    url = "https://www.reddit.com/r/" + subreddit + "/rising/.json"

agent = "Reddit Wallpaper"
r = requests.get(url, headers={"User-agent": agent})
data = json.loads(r.content)

img_url = ""
for child in data["data"]["children"]:
    url = child["data"]["url"]
    if url[-3:] in filetypes:
        img_url = url
        print(img_url)
        break

img_data = requests.get(img_url).content
file_name = "wallpaper" + img_url[-4:]
with open(file_name, "wb") as file:
    file.write(img_data)

img_path = os.path.join(os.getcwd(), file_name)
ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)
