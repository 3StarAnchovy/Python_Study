#요건 내일
import requests

api_key = "RGAPI-cce887fb-67e8-487a-a70d-2476970599c2"
url ="https://kr.api.riotgames.com"+"/lol/summoner/v4/summoners/by-name/"+"HongJiMin"+"?api_key="+api_key
res = requests.get(url)

print(res.json())