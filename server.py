from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

def append_to_json_file(filename, new_data):
    """Ajoute les données à un fichier JSON existant, ou en crée un."""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(new_data)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/submit-reservation', methods=['POST'])
def submit_reservation():
    data = request.json
    print("Réservation reçue :", data)
    append_to_json_file('reservations.json', data)
    return jsonify({"message": "Réservation enregistrée"}), 200

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    data = request.json
    print("Message de contact reçu :", data)
    append_to_json_file('contacts.json', data)
    return jsonify({"message": "Message reçu"}), 200

if __name__ == '__main__':
    app.run(port=5000)
