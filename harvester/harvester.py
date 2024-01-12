# harvester/harvester.py
import nmap

def scan_network():
    # Créer une instance de l'objet de scan Nmap
    nm = nmap.PortScanner()

    # Spécifier la plage d'adresses IP à scanner
    # Vous pouvez remplacer la plage par celle de votre réseau
    scan_result = nm.scan(hosts='192.168.1.1/24', arguments='-sP')

    # Traiter les résultats du scan
    machines = []
    for host, info in scan_result['scan'].items():
        machine_info = {
            'ip_address': host,
            'status': info['status']['state'],
            # Ajouter d'autres informations si nécessaire
        }
        machines.append(machine_info)

    return machines

if __name__ == "__main__":
    # Exemple d'utilisation
    scanned_machines = scan_network()
    for machine in scanned_machines:
        print(f"IP Address: {machine['ip_address']}, Status: {machine['status']}")
