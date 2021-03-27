import requests
import json

url = "http://ddragon.leagueoflegends.com/cdn/11.6.1/data/ko_KR/champion.json"
req = requests.get(url)
print(req.json().get("data"))

#get("key")