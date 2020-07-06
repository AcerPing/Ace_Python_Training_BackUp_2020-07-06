from sys import argv as sysArgs
import webbrowser

try:
    #獲取系統變數
    # sysArgs = sys.argv          #系統變數argv
    argsCount = len(sysArgs)    #系統變數數量(檢查用)
    print(f"Arguments count: {argsCount}")
    
    #判斷變數是否小於1
    if argsCount <= 1 :
        print("網址尚未輸入，請輸入網址！")
    
    #開啟網頁
    else:        
        for arg in sysArgs[1:]:
            print(f"開啟網頁:{str(arg)}")
            web=webbrowser.get('windows-default')
            web.open(arg)

except Exception as e:
	print("Error---Exception:", e)
else:
	print("Ok")
finally:
	print("Finish")
