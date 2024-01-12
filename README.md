# MSPR_BKRR

# Seahawks Monitoring

## Description

"Seahawks Monitoring" est un projet développé par NFL IT pour améliorer la maintenance à distance des infrastructures informatiques des franchises de la National Football League (NFL). L'application se compose du "Seahawks Harvester" (côté client) et du "Seahawks Nester" (côté serveur), offrant des fonctionnalités de supervision, et de remontée d'informations techniques sur les réseaux des franchises.

## Fonctionnalités Principales

- **Scan Réseau (Harvester)** : Utilisation du module Nmap Python pour récolter des informations sur les machines connectées.
- **Tableau de Bord (Web GUI)** : Affichage des informations clés telles que l'adresse IP, les machines connectées, les résultats du scan, etc.
- **Communication Harvester-Nester** : Utilisation d'une API pour transférer et afficher les données entre le Harvester et le Nester.
- **Base de Données** : Utilisation de MariaDB pour stocker les données.

## Structure du Projet

 SeahawksMonitoring/
├── harvester/
│   ├── harvester.py
├── nester/
│   ├── nester.py
│   └── database.sql
├── web_gui/
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   └── dashboard.html
│   └── web_gui.py
├── main.py

## Installation et Exécution

1. Installez les dépendances en utilisant la commande suivante :

   ```bash
   pip install -r requirements.txt
   
2. Exécutez l'application en lançant le fichier main.py :
   python main.py

3. Accédez au tableau de bord dans votre navigateur à l'adresse http://127.0.0.1:5000/.

4. Configuration
   Assurez-vous d'avoir une base de données MariaDB configurée et prête à être utilisée.
   Modifiez les paramètres du scan réseau dans le fichier harvester/harvester.py en fonction de votre réseau.


## Contributeurs

BLucas (@lucas03481)
KFarès (@fares2k)
RGuillaume (@guillaumerelys)
RFlorent (@Friviere7)


