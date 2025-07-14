from core.port_scanner import scan_ports

def run_scan(command):
    try:
        _, ip, port_range = command.split()
        start, end = map(int, port_range.split("-"))
        print(f"\033[94m[*] Escaneando {ip} desde el puerto {start} hasta el {end}...\033[0m")
        open_ports = scan_ports(ip, start, end)
        if open_ports:
            print("\033[92m[+] Puertos abiertos:\033[0m")
            for port in open_ports:
                print(f"  -> {port}")
        else:
            print("\033[93m[-] No se encontraron puertos abiertos.\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Error al ejecutar el escaneo: {e}\033[0m")
