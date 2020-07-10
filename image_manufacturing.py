import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

image = input("請輸入圖片檔名：")
font = input("請輸入浮水印內容：")
fontsize = int(input("請輸入浮水印尺寸"))

pic = cv2.imread(image,1) #讀取一張圖像

set = ImageFont.truetype("msjh.ttc", fontsize) #TTF字型檔設定(含文字大小)
pic = Image.fromarray(pic) #將CV圖像變數存為PIL圖像變數
ImageDraw.Draw(pic).text((0,0), font, (150,150,150), set)
pic = np.array(pic) #再將PIL圖像變數存為CV圖像變數

cv2.imshow("img",pic) #顯示圖片
cv2.waitKey() #等待按鍵繼續執行
cv2.destroyAllWindows #關閉所有視窗
