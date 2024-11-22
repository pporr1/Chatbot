from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton,
    MessageAction, CameraAction, CameraRollAction, LocationAction,
    PostbackAction, DatetimePickerAction, FlexSendMessage, URIAction
)

# ค่าคอนฟิก
LINE_CHANNEL_ACCESS_TOKEN = "GSjV7n/15Cucn66H1TCXPV1F/GoklTZxI/pTCrdevhD1M69V306HHKh27ce2D1wohujGNp2dMApGqo80mcvYEwl1IKKXqBVpr+YXnpB6V1noFkMXBANgPpejVhKvs6nKDG0FEcmNHaxprJV836R5fgdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "dc1be297b717f7750aefdaf524d580b9"


app = Flask(__name__)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

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
                            "label": "หัวข้อใหญ่ 1",
                            "text": "หัวข้อใหญ่ 1"
                        }
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "หัวข้อใหญ่ 2",
                            "text": "หัวข้อใหญ่ 2"
                        }
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "หัวข้อใหญ่ 3",
                            "text": "หัวข้อใหญ่ 3"
                        }
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "หัวข้อใหญ่ 4",
                            "text": "หัวข้อใหญ่ 4"
                        }
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "หัวข้อใหญ่ 5",
                            "text": "หัวข้อใหญ่ 5"
                        }
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "หัวข้อใหญ่ 6",
                            "text": "หัวข้อใหญ่ 6"
                        }
                    }
                ]
            }
        }
    )
    line_bot_api.reply_message(event.reply_token, flex_message)

# ฟังก์ชันแสดงข้อย่อยเมื่อเลือกหัวข้อใหญ่
def handle_subtopics(event, main_topic):
    subtopics = []
    if main_topic == "หัวข้อใหญ่ 1":
        subtopics = [
            {"label": "ย่อย 1", "url": "https://www.example1.com"},
            {"label": "ย่อย 2", "url": "https://www.example2.com"},
            {"label": "ย่อย 3", "url": "https://www.example3.com"},
            {"label": "ย่อย 4", "url": "https://www.example4.com"}
        ]
    elif main_topic == "หัวข้อใหญ่ 2":
        subtopics = [
            {"label": "ย่อย 1", "url": "https://www.example5.com"},
            {"label": "ย่อย 2", "url": "https://www.example6.com"},
            {"label": "ย่อย 3", "url": "https://www.example7.com"},
            {"label": "ย่อย 4", "url": "https://www.example8.com"}
        ]
    # ... เพิ่มกรณีของหัวข้อใหญ่ที่เหลือตามต้องการ

    # สร้าง Flex Message สำหรับข้อย่อย
    subtopic_buttons = []
    for sub in subtopics:
        subtopic_buttons.append({
            "type": "button",
            "style": "secondary",
            "action": {
                "type": "uri",
                "label": sub["label"],
                "uri": sub["url"]
            }
        })

    flex_message = FlexSendMessage(
        alt_text="Subtopics",
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": subtopic_buttons
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
    if event.message.text.startswith("หัวข้อใหญ่"):
        handle_subtopics(event, event.message.text)
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="ไม่เข้าใจคำสั่ง!")
        )

# รันเซิร์ฟเวอร์
if __name__ == "__main__":
    app.run(port=8000)
