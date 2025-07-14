### 🐒 Monkey - Port Scanner CLI Tool

### main.py
from core.command_processor import start_cli

if __name__ == "__main__":
    start_cli()


### core/command_processor.py
def show_banner():
    banner = r'''
     __  __             _        
    |  \/  | ___  _ __ | | ___   
    | |\/| |/ _ \| '_ \| |/ _ \  
    | |  | | (_) | | | | |  __/  
    |_|  |_|\___/|_| |_|_|\___|  

         🐒 Monkey Port Scanner
    '''
    print("\033[96m" + banner + "\033[0m")

def start_cli():
    show_banner()
    print("Escribe 'scan [IP] [rango]' o 'exit' para salir")
    while True:
        try:
            cmd = input("monkey > ").strip()
            if cmd == "exit":
                break
            elif cmd.startswith("scan"):
                from commands.scan import run_scan
                run_scan(cmd)
            else:
                print("\033[91m[!] Comando no reconocido.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[93m[!] Saliendo de Monkey...\033[0m")
            break



from core.scan.py import scan_port

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


### core/port_scanner.py
import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                return port
    except:
        pass
    return None

def scan_ports(ip, start, end):
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(ip, p), range(start, end + 1))
    return [port for port in results if port is not None]
