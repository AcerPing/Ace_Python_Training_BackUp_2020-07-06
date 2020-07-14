from linebot import (LineBotApi)
from linebot.models import (RichMenu)
import json

#TODO:創造line_bot_api
line_bot_api = LineBotApi('EHs7+foRB5Ucx23bz14MKwzAePKbJDeonDsOMOlcksS1MFk1cZ3jFjdbQz5iHFUsi1RpecUtZCGfn25PWkM8Ftz2e3zSE9KttGtXMxULdKUlI/Hk9czu5BYm+uZzjdITSY2j7w+QMDZX950H4ML7dwdB04t89/1O/w1cDnyilFU=')

'''
#TODO:將設定檔傳給line
# 讀取json檔
# 轉成json格式
# 將json格式做成RichMenu的變數
# line_bot_api傳給line
# 把rich_menu_id打印出來
with open("rich_menu.json","r",encoding="utf8") as json_file:
    rich_menu_json_object = json.load(json_file)
#TODO:將json格式做成RichMenu的變數
rich_menu_config = RichMenu.new_from_json_dict(rich_menu_json_object)

#TODO:line_bot_api傳給line
rich_menu_id = line_bot_api.create_rich_menu(rich_menu_config)

#TODO:把rich_menu_id打印出來
print(rich_menu_id)
'''
'''
#TODO:把照片傳給指定的圖文選單id
# 準備圖片
# 把圖片載入
# 命令line_bot_api將圖片上傳到指定圖文選單的id上
rich_menu_id ="richmenu-b7095794c64a7bf1784f0959a33b6c05"
with open("rich_menu.jpg","rb") as image_file:
    response = line_bot_api.set_rich_menu_image(
        rich_menu_id = rich_menu_id,
        content_type = "image/jpeg",
        content = image_file)

print(response)
'''
'''
#TODO:綁定用戶與圖文選單
rich_menu_id ="richmenu-b7095794c64a7bf1784f0959a33b6c05"
line_bot_api.link_rich_menu_to_user(
    user_id="Ufceff163313e89e97b772ecd525c35d1",
    rich_menu_id = rich_menu_id)
'''
'''
#TODO:解除
line_bot_api.unlink_rich_menu_from_user(
    user_id="Ufceff163313e89e97b772ecd525c35d1")
'''
#TODO:刪除圖文選單
rich_menu_id ="richmenu-b7095794c64a7bf1784f0959a33b6c05"
line_bot_api.delete_rich_menu(rich_menu_id=rich_menu_id)

