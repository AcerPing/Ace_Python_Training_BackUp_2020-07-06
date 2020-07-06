#網路連線
# import urllib.request as request
# URL="https://www.jlpt.tw/"
# with request.urlopen(URL) as response:
#     data=response.read().decode("utf-8") #取得網站的原始碼
# print(data)

#串接、擷取公開資料
import urllib.request as request
import json
URL="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(URL) as response:
    data=json.load(response) #利用JSON模組處理JSON格式資料
clist=data["result"]["results"]
# print(clist)
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")
        # print(company["公司名稱"])
