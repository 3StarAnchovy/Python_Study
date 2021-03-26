#요건 내일

import requests
class RiotData:
    def __init__(self,userID): #set
        self.userID=userID
        self.api_key = "RGAPI-cce887fb-67e8-487a-a70d-2476970599c2"
        self.url="https://kr.api.riotgames.com"
    def getUserData(self): #유저 정보
        url = self.url+"/lol/summoner/v4/summoners/by-name/"+self.userID+"?api_key="+self.api_key
        res = requests.get(url)
        return res

userID = input("userID : ")
test = RiotData(userID)
print(test.getUserData().json())

#api_key = "RGAPI-cce887fb-67e8-487a-a70d-2476970599c2"
#url ="https://kr.api.riotgames.com"+"/lol/summoner/v4/summoners/by-name/"+"HongJiMin"+"?api_key="+api_key
#res = requests.get(url)