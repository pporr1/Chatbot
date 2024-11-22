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

# ฟังก์ชันสำหรับการเริ่มต้น
def handle_start(event):
    # สร้างเมนูหัวข้อใหญ่ 6 ข้อ
    flex_message = FlexSendMessage(
        alt_text="เลือกหัวข้อใหญ่",
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#FFCC00",  # สีเหลือง
                        "action": {
                            "type": "message",
                            "label": "หัวข้อใหญ่ 1",
                            "text": "หัวข้อใหญ่ 1"
                        },
                        "margin": "sm",
                        "height": "sm",
                        "gravity": "center"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#FFCC00",  # สีเหลือง
                        "action": {
                            "type": "message",
                            "label": "หัวข้อใหญ่ 2",
                            "text": "หัวข้อใหญ่ 2"
                        },
                        "margin": "sm",
                        "height": "sm",
                        "gravity": "center"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#FFCC00",  # สีเหลือง
                        "action": {
                            "type": "message",
                            "label": "หัวข้อใหญ่ 3",
                            "text": "หัวข้อใหญ่ 3"
                        },
                        "margin": "sm",
                        "height": "sm",
                        "gravity": "center"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#FFCC00",  # สีเหลือง
                        "action": {
                            "type": "message",
                            "label": "หัวข้อใหญ่ 4",
                            "text": "หัวข้อใหญ่ 4"
                        },
                        "margin": "sm",
                        "height": "sm",
                        "gravity": "center"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#FFCC00",  # สีเหลือง
                        "action": {
                            "type": "message",
                            "label": "หัวข้อใหญ่ 5",
                            "text": "หัวข้อใหญ่ 5"
                        },
                        "margin": "sm",
                        "height": "sm",
                        "gravity": "center"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#FFCC00",  # สีเหลือง
                        "action": {
                            "type": "message",
                            "label": "หัวข้อใหญ่ 6",
                            "text": "หัวข้อใหญ่ 6"
                        },
                        "margin": "sm",
                        "height": "sm",
                        "gravity": "center"
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
    elif main_topic == "หัวข้อใหญ่ 3":
        subtopics = [
            {"label": "ย่อย 1", "url": "https://www.example9.com"},
            {"label": "ย่อย 2", "url": "https://www.example10.com"},
            {"label": "ย่อย 3", "url": "https://www.example11.com"},
            {"label": "ย่อย 4", "url": "https://www.example12.com"}
        ]
    elif main_topic == "หัวข้อใหญ่ 4":
        subtopics = [
            {"label": "ย่อย 1", "url": "https://www.example13.com"},
            {"label": "ย่อย 2", "url": "https://www.example14.com"},
            {"label": "ย่อย 3", "url": "https://www.example15.com"},
            {"label": "ย่อย 4", "url": "https://www.example16.com"}
        ]
    elif main_topic == "หัวข้อใหญ่ 5":
        subtopics = [
            {"label": "ย่อย 1", "url": "https://www.example17.com"},
            {"label": "ย่อย 2", "url": "https://www.example18.com"},
            {"label": "ย่อย 3", "url": "https://www.example19.com"},
            {"label": "ย่อย 4", "url": "https://www.example20.com"}
        ]
    elif main_topic == "หัวข้อใหญ่ 6":
        subtopics = [
            {"label": "ย่อย 1", "url": "https://www.example21.com"},
            {"label": "ย่อย 2", "url": "https://www.example22.com"},
            {"label": "ย่อย 3", "url": "https://www.example23.com"},
            {"label": "ย่อย 4", "url": "https://www.example24.com"}
        ]

    # สร้าง Flex Message สำหรับข้อย่อย
    subtopic_buttons = []
    for sub in subtopics:
        subtopic_buttons.append({
            "type": "button",
            "style": "secondary",
            "color": "#A6A6A6",  # สีเทา
            "action": {
                "type": "uri",
                "label": sub["label"],
                "uri": sub["url"]
            },
            "margin": "sm",
            "height": "sm",
            "gravity": "center"
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
    if event.message.text == "เริ่มต้น":
        handle_start(event)
    elif event.message.text.startswith("หัวข้อใหญ่"):
        handle_subtopics(event, event.message.text)
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="กรุณาพิมพ์ 'เริ่มต้น' เพื่อเริ่มเลือกหัวข้อใหญ่")
        )

if __name__ == "__main__":
    app.run(debug=True)
