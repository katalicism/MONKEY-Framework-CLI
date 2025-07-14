import socket

def run_scan(ip):
    print(f"Iniciando escaneo de puertos en {ip}...")
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "desconocido"
            print(f"Puerto {port} abierto - Servicio: {service}")
        sock.close()
    print("Escaneo terminado.")
