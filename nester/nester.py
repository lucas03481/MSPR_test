# nester/nester.py
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuration de la base de données
db = mysql.connector.connect(
    host="votre_host",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    database="votre_base_de_donnees"
)
cursor = db.cursor()

# API pour recevoir les données du Harvester
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()

    # Exemple : Enregistrez les données dans la base de données
    ip_address = data.get('ip_address')
    machine_name = data.get('machine_name')
    timestamp = data.get('timestamp')
    device_type = data.get('device_type')
    numero_port = data.get('numero_port')
    flux = data.get('flux')
    nbr_port_ouvert = data.get('nbr_port_ouvert')
    scan_results = data.get('scan_results')

    # Exécutez la requête SQL pour insérer les données dans la base de données
    insert_query = """
    INSERT INTO machines_v2 
    (ip_address, machine_name, timestamp, device_type, numero_port, flux, nbr_port_ouvert, scan_results) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (ip_address, machine_name, timestamp, device_type, numero_port, flux, nbr_port_ouvert, scan_results)
    cursor.execute(insert_query, values)
    db.commit()

    return jsonify({'message': 'Données enregistrées avec succès'})

if __name__ == '__main__':
    app.run(debug=True)
