#요건 내일

import requests
class RiotData:
    def __init__(self,userID): #set
        self.userID=userID
        self.api_key = "RGAPI-370880ec-74b6-4987-b0ed-868dc79cb5bd"
        self.url="https://kr.api.riotgames.com"
        self.DataDragon = "http://ddragon.leagueoflegends.com/cdn/11.6.1/data/ko_KR/" #게임내 정적 컨텐츠
    def getUserData(self): #유저 정보
        url = self.url+"/lol/summoner/v4/summoners/by-name/"+self.userID+"?api_key="+self.api_key
        res = requests.get(url)
        return res
    def getChampRotation(self): #챔프 로테이션 출력
        url = self.url+"/lol/platform/v3/champion-rotations"+"?api_key="+self.api_key
        DataDragon_url = self.DataDragon+"champion.json"
        data_res = requests.get(DataDragon_url)
        res = requests.get(url)
        
        return res

userID = input("userID : ")
test = RiotData(userID)
print(test.getUserData().json())
print("\n")
print(test.getChampRotation().json())

#api_key = "RGAPI-cce887fb-67e8-487a-a70d-2476970599c2"
#url ="https://kr.api.riotgames.com"+"/lol/summoner/v4/summoners/by-name/"+"HongJiMin"+"?api_key="+api_key
#res = requests.get(url)