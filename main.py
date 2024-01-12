# main.py

# Importer les modules ou les fonctions nécessaires
from harvester.harvester import scan_network
from nester.nester import app as nester_app
from web_gui import app as web_gui_app

# Autres imports et configurations...

def main():
    # Tâches d'initialisation ou de configuration si nécessaire

    # Démarrer le Harvester
    scan_results = scan_network()

    # Démarrer le Nester (peut être exécuté dans un thread séparé)
    # ...

    # Démarrer le Web GUI
    web_gui_app.run(debug=True)

if __name__ == "__main__":
    main()
