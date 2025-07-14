from core.scanner import run_scan

def run_command(cmd: str):
    parts = cmd.split()
    if not parts:
        return
    command = parts[0].lower()
    args = parts[1:]

    if command == "scan":
        if len(args) != 1:
            print("Uso: scan <IP>")
            return
        ip = args[0]
        try:
            run_scan(ip)
        except Exception as e:
            print(f"[!] Error al ejecutar el escaneo: {e}")
    elif command == "help":
        print("Comandos disponibles: scan <IP>, exit, help")
    else:
        print(f"Comando desconocido: {command}")
