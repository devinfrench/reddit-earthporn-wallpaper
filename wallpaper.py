import requests
import json
import ctypes
import os

url = "https://www.reddit.com/r/earthporn/.json"
agent = "EarthPorn Wallpaper"
r = requests.get(url, headers={"User-agent": agent})
data = json.loads(r.content)
img_url = data["data"]["children"][0]["data"]["url"]
img_data = requests.get(img_url).content
file_name = "wallpaper" + img_url[-4:]
with open(file_name, "wb") as file:
    file.write(img_data)

img_path = os.path.join(os.getcwd(), file_name)
ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)
