import requests
import json
import ctypes
import os

filetypes = ["jpg", "png"]
subreddit = "wallpapers"

url = "https://www.reddit.com/r/" + subreddit + "/.json"
agent = "Reddit Wallpaper"
r = requests.get(url, headers={"User-agent": agent})
data = json.loads(r.content)

img_url = ""
for child in data["data"]["children"]:
    url = child["data"]["url"]
    if url[-3:] in filetypes:
        img_url = url
        break

img_data = requests.get(img_url).content
file_name = "wallpaper" + img_url[-4:]
with open(file_name, "wb") as file:
    file.write(img_data)

img_path = os.path.join(os.getcwd(), file_name)
ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)
