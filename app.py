from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, 
    MessageAction, CameraAction, CameraRollAction, LocationAction, 
    PostbackAction, DatetimePickerAction, FlexSendMessage
)

# ค่าคอนฟิก
LINE_CHANNEL_ACCESS_TOKEN = "GSjV7n/15Cucn66H1TCXPV1F/GoklTZxI/pTCrdevhD1M69V306HHKh27ce2D1wohujGNp2dMApGqo80mcvYEwl1IKKXqBVpr+YXnpB6V1noFkMXBANgPpejVhKvs6nKDG0FEcmNHaxprJV836R5fgdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "dc1be297b717f7750aefdaf524d580b9"

app = Flask(__name__)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# ฟังก์ชันสำหรับ Quick Reply
def handle_quick_reply(event):
    quick_reply = QuickReply(items=[
        QuickReplyButton(action=MessageAction(label="ข้อความ", text="Hello World!")),
        QuickReplyButton(action=CameraAction(label="กล้องถ่ายรูป")),
        QuickReplyButton(action=CameraRollAction(label="เลือกรูปภาพจากแกลลอรี")),
        QuickReplyButton(action=LocationAction(label="ส่งพิกัดที่อยู่")),
        QuickReplyButton(action=PostbackAction(label="Postback", data="action=buy&itemid=123", display_text="Buy")),
        QuickReplyButton(action=DatetimePickerAction(
            label="เลือกวันและเวลา", data="storeId=12345", mode="datetime",
            initial="2023-11-21T00:00", max="2023-12-31T23:59", min="2023-01-01T00:00"
        ))
    ])

    message = TextSendMessage(
        text="กรุณาเลือกรายการ",
        quick_reply=quick_reply
    )
    line_bot_api.reply_message(event.reply_token, message)

# ฟังก์ชันสำหรับ Flex Message
def handle_flex_message(event):
    flex_message = FlexSendMessage(
        alt_text="Flex Message",
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "มัธยมศึกษาปีที่ 1",
                            "text": "มัธยมศึกษาปีที่ 1"
                        }
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "มัธยมศึกษาปีที่ 2",
                            "text": "มัธยมศึกษาปีที่ 2"
                        }
                    }
                ]
            }
        }
    )
    line_bot_api.reply_message(event.reply_token, flex_message)

# Route สำหรับ Webhook
@app.route("/webhook", methods=['POST'])
def webhook():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return "Invalid signature", 400

    return "OK", 200

# Event Handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "Quick Reply":
        handle_quick_reply(event)
    elif event.message.text == "Flex Message":
        handle_flex_message(event)
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="ไม่เข้าใจคำสั่ง!")
        )

# รันเซิร์ฟเวอร์
if __name__ == "__main__":
    app.run(port=8000)
