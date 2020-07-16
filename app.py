from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi(
    'EHs7+foRB5Ucx23bz14MKwzAePKbJDeonDsOMOlcksS1MFk1cZ3jFjdbQz5iHFUsi1RpecUtZCGfn25PWkM8Ftz2e3zSE9KttGtXMxULdKUlI/Hk9czu5BYm+uZzjdITSY2j7w+QMDZX950H4ML7dwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('aea331bd7df6b63d486271a43028bf8c')

import boto3

# TODO:創建s3的客戶端
s3_client = boto3.client('s3',
                         aws_access_key_id="AKIAR4NDUH53GWDLQFNM",
                         aws_secret_access_key="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")


@app.route('/')
def hello():
    return "Hello World!"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


'''
告知handler，收到圖片消息
    要從line上把圖片抓回來
    並且檔名要以消息id為命名
    把檔案上傳到s3，位置student_30_Ace/消息id.jpg
'''


@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    # TODO:請line_bot_api抓圖片回來
    image_temp_variable = line_bot_api.get_message_content(event.message.id)

    # TODO:把圖片存成檔案
    with open(event.message.id + ".jpg", "wb") as f:
        for chunk in image_temp_variable.iter_content():
            f.write(chunk)

    response = s3_client.upload_file(event.message.id + ".jpg"
                                     , "iii-tutorial-v2"
                                     , "student_30_Ace/" + event.message.id + ".jpg")

    # TODO:line_bot_api回覆信息
    line_bot_api.reply_message(event.reply_token, TextSendMessage(event.message.id))


# if __name__ == "__main__":
#     print('X'*100)
#     app.run(host='0.0.0.0')

# TODO: heroku專用，偵測heroku給我們的port號
import os
app.run(host='0.0.0.0', port=os.environ['PORT'])
