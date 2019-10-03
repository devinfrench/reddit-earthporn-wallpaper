import requests
import json

url = "https://www.reddit.com/r/earthporn/.json"
agent = "EarthPorn Wallpaper"
r = requests.get(url, headers={"User-agent": agent})
data = json.loads(r.content)
img_url = data["data"]["children"][0]["data"]["url"]
img_data = requests.get(img_url).content
with open("wallpaper" + img_url[-4:], "wb") as file:
    file.write(img_data)
