from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, URIAction
)

app = Flask(__name__)

# Channel Secret และ Access Token
line_bot_api = LineBotApi('GSjV7n/15Cucn66H1TCXPV1F/GoklTZxI/pTCrdevhD1M69V306HHKh27ce2D1wohujGNp2dMApGqo80mcvYEwl1IKKXqBVpr+YXnpB6V1noFkMXBANgPpejVhKvs6nKDG0FEcmNHaxprJV836R5fgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('dc1be297b717f7750aefdaf524d580b9')

@app.route("/webhook", methods=['POST'])
def webhook():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return 'Invalid signature', 400

    return 'OK', 200

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    
    # เมื่อผู้ใช้ส่งข้อความ ให้แสดงตัวเลือก
    if user_message == "เริ่มต้น":
        reply = TemplateSendMessage(
            alt_text="กรุณาเลือกหมวดหมู่",
            template=ButtonsTemplate(
                title="เลือกหมวดหมู่",
                text="กรุณาเลือกหมวดหมู่ที่ต้องการ",
                actions=[
                    MessageTemplateAction(label="หมวด 1", text="เลือกหมวด 1"),
                    MessageTemplateAction(label="หมวด 2", text="เลือกหมวด 2")
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, reply)
    
    # หากผู้ใช้เลือก "หมวด 1"
    elif user_message == "เลือกหมวด 1":
        reply = TemplateSendMessage(
            alt_text="เลือกตัวเลือกในหมวด 1",
            template=ButtonsTemplate(
                title="ตัวเลือกในหมวด 1",
                text="กรุณาเลือก",
                actions=[
                    URIAction(label="ไปที่เว็บ 1", uri="https://example.com/1"),
                    URIAction(label="ไปที่เว็บ 2", uri="https://example.com/2")
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, reply)
    
    # หากผู้ใช้เลือก "หมวด 2"
    elif user_message == "เลือกหมวด 2":
        reply = TemplateSendMessage(
            alt_text="เลือกตัวเลือกในหมวด 2",
            template=ButtonsTemplate(
                title="ตัวเลือกในหมวด 2",
                text="กรุณาเลือก",
                actions=[
                    URIAction(label="ไปที่เว็บ 3", uri="https://example.com/3"),
                    URIAction(label="ไปที่เว็บ 4", uri="https://example.com/4")
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, reply)

if __name__ == "__main__":
    app.run(port=8000)
