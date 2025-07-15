from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

@app.route("/updates")
def get_updates():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    resp = requests.get(url)
    data = resp.json()
    messages = []

    if data.get("ok"):
        for update in data["result"]:
            msg = update.get("message", {}).get("text", "")
            chat_id = update.get("message", {}).get("chat", {}).get("username", "")
            if msg.endswith("#Обновление") and (chat_id == CHANNEL_ID.replace("@", "")):
                messages.append(msg)

    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
