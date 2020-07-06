# #方法一:import webbrowser，使用預設瀏覽器執行
# import webbrowser
# Address=input("アドレスを入力して下さい：")
# webbrowser.open(Address)

#方法二:使用sys.argv，讓預設瀏覽器執行網址
import webbrowser
from sys import argv
webbrowser.open(argv[1])



