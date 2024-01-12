import socket
import ipaddress
import concurrent.futures

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def scan_ip_range(start_ip, end_ip):
    print(f"Scanning IP range: {start_ip} to {end_ip}")
    start_ip = ipaddress.IPv4Address(start_ip)
    end_ip = ipaddress.IPv4Address(end_ip)
    active_ips = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for ip_int in range(int(start_ip), int(end_ip) + 1):
            ip = str(ipaddress.IPv4Address(ip_int))
            if executor.submit(check_ip, ip).result():
                active_ips.append(ip)
    return active_ips

def check_ip(ip_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ip_address, 80))
        return True
    except:
        return False
    finally:
        sock.close()

def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning ports on {target_ip} from port {start_port} to {end_port}")
    open_ports = []
    for port in range(start_port, end_port + 1):
        if check_port(target_ip, port):
            open_ports.append(port)
    return open_ports

def check_port(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ip_address, port))
        return True
    except:
        return False
    finally:
        sock.close()

def main():
    start_ip = input("Enter the start IP for the range: ")
    if not is_valid_ip(start_ip):
        print("Invalid start IP address.")
        return

    end_ip = input("Enter the end IP for the range: ")
    if not is_valid_ip(end_ip):
        print("Invalid end IP address.")
        return

    active_ips = scan_ip_range(start_ip, end_ip)
    print(f"Active IPs in range: {active_ips}")

    target_ip = input("Enter target IP for port scanning: ")
    if not is_valid_ip(target_ip):
        print("Invalid target IP address.")
        return

    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    open_ports = scan_ports(target_ip, start_port, end_port)
    print(f"Open ports on {target_ip}: {open_ports}")

if __name__ == "__main__":
    main()