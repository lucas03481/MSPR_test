from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    # Recevoir les données du Harvester
    # Enregistrer les données dans la base de données
    pass

if __name__ == '__main__':
    app.run(debug=True)
