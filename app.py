from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from handlers import procesar

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    numero = request.form.get("From")
    body   = request.form.get("Body")

    resp = MessagingResponse()
    procesar(numero, body, resp)

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
