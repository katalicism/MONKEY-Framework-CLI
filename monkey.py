import socket
import threading
import time
import whois
from colorama import Fore, Style, init
import os
import platform
import subprocess
import requests

init(autoreset=True)

common_ports = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 3306: "MySQL", 3389: "RDP"
}

def banner_inicio():
    titulo = " MONKEY - Port Scanner "
    ancho = len(titulo) + 4  # Margen de 2 espacios a cada lado
    
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT)
    print("-" * ancho)
    print(f"|{titulo}|")
    print("-" * ancho)
    print("🔧  by katalicism02")
    print()

def scan_port(ip, port, timeout=1, open_ports=[]):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        if result == 0:
            service = common_ports.get(port, "Desconocido")
            print(Fore.GREEN + f"[+] Puerto {port} abierto ({service})")
            open_ports.append((port, service))
        sock.close()
    except:
        pass

def escanear_puertos():
    open_ports = []

    print(Fore.CYAN + "\n🔍 Escaneo de Puertos 🐒\n")
    target = input("👉 IP o dominio a escanear: ").strip()
    try:
        ip = socket.gethostbyname(target)
    except:
        ip = target

    modo = input("🚀 Modo (normal / sigiloso)? [n/s]: ").strip().lower()
    sigiloso = modo == 's'

    try:
        inicio = int(input("📍 Puerto inicial: "))
        fin = int(input("📍 Puerto final: "))
        ports = range(inicio, fin + 1)
    except:
        print(Fore.RED + "Entrada inválida. Usando puertos comunes.")
        ports = list(common_ports.keys())

    print(Fore.YELLOW + f"\n[~] Escaneando {ip}...\n")
    start = time.time()

    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(ip, port, 1 if not sigiloso else 2, open_ports))
        threads.append(t)
        t.start()
        if sigiloso:
            time.sleep(0.2)  # Delay entre hilos en modo sigiloso

    for t in threads:
        t.join()

    duration = time.time() - start
    print(Fore.CYAN + f"\n✅ Escaneo completado en {duration:.2f} s.")
    print(Fore.CYAN + f"🔓 Puertos abiertos: {len(open_ports)}")

    if open_ports:
        save = input("💾 ¿Guardar resultados? (s/n): ").lower()
        if save == "s":
            filename = f"scan_{target.replace('.', '_')}.txt"
            with open(filename, "w") as f:
                for port, service in open_ports:
                    f.write(f"Puerto {port} abierto ({service})\n")
            print(Fore.GREEN + f"📁 Guardado en {filename}")

def obtener_whois():
    print(Fore.CYAN + "\n🌐 Consulta WHOIS\n")
    domain = input("👉 Dominio o IP: ").strip()
    try:
        w = whois.whois(domain)
        print()
        for key in ['domain_name', 'registrar', 'creation_date', 'expiration_date', 'name_servers', 'emails']:
            if key in w and w[key]:
                print(Fore.MAGENTA + f"{key.replace('_', ' ').title()}: {w[key]}")
    except Exception as e:
        print(Fore.RED + f"[!] Error al obtener WHOIS: {e}")

def escanear_subdominios():
    print(Fore.CYAN + "\n🔍 Escaneo de Subdominios\n")
    domain = input("👉 Dominio objetivo: ").strip()
    subdomains = ["www", "mail", "ftp", "blog", "dev", "test", "admin"]

    encontrados = []
    for sub in subdomains:
        url = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(url)
            print(Fore.GREEN + f"[+] {url} -> {ip}")
            encontrados.append((url, ip))
        except:
            pass

    if not encontrados:
        print(Fore.YELLOW + "No se encontraron subdominios comunes.")

def ping_host():
    print(Fore.CYAN + "\n📡 Ping Host\n")
    host = input("👉 IP o dominio: ").strip()
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", host]

    try:
        output = subprocess.check_output(command, universal_newlines=True)
        print(Fore.GREEN + output)
    except subprocess.CalledProcessError:
        print(Fore.RED + "No se pudo hacer ping al host.")

def chequear_headers():
    print(Fore.CYAN + "\n🌐 Chequeo de Headers HTTP\n")
    url = input("👉 URL (con http/https): ").strip()
    try:
        respuesta = requests.head(url)
        for k, v in respuesta.headers.items():
            print(Fore.MAGENTA + f"{k}: {v}")
    except Exception as e:
        print(Fore.RED + f"Error al obtener headers: {e}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_inicio()
    while True:
        print(Fore.CYAN + "\n|=== Monkey OSINT CLI 🐒 ===|")
        print(Fore.YELLOW + "1. Escanear puertos")
        print("2. WHOIS")
        print("3. Escanear subdominios")
        print("4. Ping")
        print("5. Chequeo Headers")
        print("6. Salir")

        opcion = input(Fore.CYAN + "\nElige una opción: ").strip()

        if opcion == "1":
            escanear_puertos()
        elif opcion == "2":
            obtener_whois()
        elif opcion == "3":
            escanear_subdominios()
        elif opcion == "4":
            ping_host()
        elif opcion == "5":
            chequear_headers()
        elif opcion == "6":
            print(Fore.GREEN + "👋 ¡Hasta luego!")
            break
        else:
            print(Fore.RED + "❌ Opción no válida.")

if __name__ == "__main__":
    main()
