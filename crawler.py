import urllib.request as req
import bs4
import warnings 

#抓取PTT電影版的網頁原始碼 (HTML)
url="https://www.ptt.cc/bbs/movie/index.html"

#建立一個request物件，附加Request Headers資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"})

#讀取網頁原始碼資訊
with req.urlopen(request) as response:
    data = response.read().decode("utf8")
# print(data) 列印出網頁原始碼資料

#解析原始碼，取得每篇文章的標題
warnings.filterwarnings('ignore')  #不想看到BeautifulSoup跳出來的Warnings
root = bs4.BeautifulSoup(data) #對整份網頁原始碼資料作分析，讓BeautifulSoup協助解析HTML格式文件
# print(root.title.string) #列出title的文字

'''
titles = root.find("div",class_="title") #尋找class="title"的div標籤
print(titles.a.string) #抓取class="title"的當中a的文字
'''

titles = root.find_all("div",class_="title") #尋找所有class="title"的div標籤
print(titles) #印出所有所有class="title"的div標籤

for x in titles: #List的內容一個一個抓取出來
    if x.find("a") != None: #如果標題包含a標籤(沒有被刪除)，印出來
        print(x.find("a").attrs["href"])
        print(x.find("a").string)
