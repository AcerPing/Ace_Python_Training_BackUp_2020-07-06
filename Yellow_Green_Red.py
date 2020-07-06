import time
import os
import colorama
import prettytable
colorama.init(True) #初始化Colorama(自動清除)
# signal=prettytable.PrettyTable([" "],encoding="utf-8")
# signal.align[" "]="l"
# signal.align[" "]="c"

#首先讓signal=0，並在小於12的時候，執行while迴圈
while True:
	#讓singal從1-12的數字中一個一個抓取
	for signal in range(1,11,1):
		os.system("cls")
		#當signal小於6時(0-5)，則顯示紅燈
		if signal<6:
			# colorama.init(True) 初始化改放在外圈
			print(colorama.Back.RED+"   ")
			print(signal)
			time.sleep(1)

# 當signal等於6時，則顯示黃燈
		elif signal==6:
			# colorama.init(True) 初始化改放在外圈
			print("\t",colorama.Back.YELLOW+"   ")
			print(signal)
			time.sleep(1)

#當signal小於10時(大於6，6-10)，則顯示綠燈
	# colorama.init(True)
		elif signal<10:
			# signal.align[" "]="r"
			print("\t\t",colorama.Back.GREEN+"   ")
			print(signal)
			time.sleep(1)

#當singal等於10時，顯示綠燈，但秒數為0
		elif signal==10:
			print("\t\t",colorama.Back.GREEN+"   ")
			print("0")
			time.sleep(1)

