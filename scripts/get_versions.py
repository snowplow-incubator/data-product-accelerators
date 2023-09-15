import requests
import json
import time

with open("data/component_versions.json") as jsonFile:
    data = json.load(jsonFile)

temp_json = data

for package in temp_json["packages"]:
    res = requests.get("https://api.github.com/repos" + package["url"])
    version = res.json()["tag_name"]
    package["version"] = version

temp_json["last_update"] = time.time()
jsonFile = open("data/component_versions.json", "w+")
jsonFile.write(json.dumps(temp_json))
jsonFile.close()
