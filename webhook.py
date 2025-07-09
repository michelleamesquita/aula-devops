from flask import Flask, request
import requests
import os

TOKEN = os.getenv("TOKEN")

app = Flask(__name__)

@app.route('/')
def home():
    return 'Webhook Flask App rodando!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print('Recebido:', data)
    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]
       
        send_message(chat_id, f"Você disse: {text}")
    return {"ok": True}

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(debug=True)
