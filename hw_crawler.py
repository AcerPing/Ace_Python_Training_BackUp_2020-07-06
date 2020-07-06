import requests

url="http://teaching.bo-yuan.net/test/requests/?action=GoToJapan"

#TODO 使用requests，並使用codecs.open打開檔案，同時utf8進行解碼

#使用requests開啟url
response=requests.post(url,data={"id":"ace","name":"ace","address":"japan"}) #讀取指定網址
# print(response) #顯示<Response [200]> → 讀取成功
response.encoding = "utf8" #讀取和設定編碼

print(response.text) #讀取(顯示)內容 以純文字型態讀取，會自動做編碼的轉換


'''
解題祕訣：
缺少參數「action」 → 將網址改為"http://teaching.bo-yuan.net/test/requests/?action=GoToJapan"(原網址接上參數(?action=GoToJapan))
此時會顯示需要DELETE的操作 → requests.delete
缺少資料「id」→ data={"id":"ace"}
記得去PUT操作 → requests.put
需要更新資料「name」→ data={"id":"ace","name":"ace"}
需要PATCH的資料是「address」→ requests.patch ; data={"id":"ace","name":"ace","address":"japan"}
最後POST一筆資料吧 → requests.post
'''


'''
【Draft】
import codecs
#先寫入檔案
with codecs.open("homework-crawler-2.html","w",encoding="utf-8") as file:
	file.write(response.text) #寫入內容 以純文字型態讀取，會自動做編碼的轉換
#再讀取檔案
with codecs.open("homework-crawler-2.html","r",encoding="utf-8") as file:
	print(file.read())
'''
















