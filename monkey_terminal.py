from colorama import Fore, Style, init
init(autoreset=True)

def mostrar_caja_inicio():
    caja = [
        Fore.CYAN + "=====================================" + Style.RESET_ALL,
        Fore.CYAN + "| " + Fore.YELLOW + "🐒 MONKEY - Framework CLI" + Fore.CYAN + "                |" + Style.RESET_ALL,
        Fore.CYAN + "=====================================" + Style.RESET_ALL,
        "🔧  by katalicism",
        "",
        Fore.MAGENTA + "|=== Monkey OSINT CLI 🐒 ===|" + Style.RESET_ALL,
        Fore.GREEN + "Comandos disponibles:" + Style.RESET_ALL,
        Fore.GREEN + " | scan [IP] [puerto_inicio] [puerto_fin]  " + Fore.WHITE + "- Escanea puertos TCP en un rango" + Style.RESET_ALL,
        Fore.GREEN + " | whois [dominio]                        " + Fore.WHITE + "- Consulta WHOIS del dominio" + Style.RESET_ALL,
        Fore.GREEN + " | subdomains [dominio]                   " + Fore.WHITE + "- Busca subdominios del dominio" + Style.RESET_ALL,
        Fore.GREEN + " | ping [IP/dominio]                      " + Fore.WHITE + "- Envía ping al objetivo" + Style.RESET_ALL,
        Fore.GREEN + " | headers [dominio]                      " + Fore.WHITE + "- Muestra headers HTTP" + Style.RESET_ALL,
        Fore.GREEN + " | exit                                  " + Fore.WHITE + "- Salir del programa" + Style.RESET_ALL,
        "",
        Fore.RED + "⚠️  Usa esta herramienta de forma ética y responsable, no nos hacemos responsables de cualquier uso fraudulento." + Style.RESET_ALL,
        "",
    ]
    for linea in caja:
        print(linea)

def main():
    mostrar_caja_inicio()

    while True:
        entrada = input(Fore.GREEN + "msfadmin" + Fore.YELLOW + "> " + Style.RESET_ALL).strip()
        if not entrada:
            continue
        comando, *args = entrada.split()

        if comando == "exit":
            print("Saliendo de Monkey...")
            break
        elif comando == "scan":
            if len(args) != 3:
                print("Uso: scan [IP] [puerto_inicio] [puerto_fin]")
                continue
            ip, puerto_inicio, puerto_fin = args
            print(f"🐒Escaneando puertos de {ip} desde {puerto_inicio} hasta {puerto_fin}...")
            # Aquí va tu función de escaneo
        elif comando == "whois":
            if len(args) != 1:
                print("Uso: whois [dominio]")
                continue
            dominio = args[0]
            print(f"Consultando WHOIS para {dominio}...")
            # Aquí tu función whois
        elif comando == "subdomains":
            if len(args) != 1:
                print("Uso: subdomains [dominio]")
                continue
            dominio = args[0]
            print(f"🐒Buscando subdominios de {dominio}...")
            # Aquí función subdominios
        elif comando == "ping":
            if len(args) != 1:
                print("Uso: ping [IP/dominio]")
                continue
            objetivo = args[0]
            print(f"Haciendo ping a {objetivo}...")
            # Aquí función ping
        elif comando == "headers":
            if len(args) != 1:
                print("Uso: headers [dominio]")
                continue
            dominio = args[0]
            print(f"Chequeando headers HTTP de {dominio}...")
            # Aquí función headers
        else:
            print("Comando no reconocido. Escribe 'exit' para salir.")

if __name__ == "__main__":
    main()
