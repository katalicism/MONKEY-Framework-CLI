# MONKEY - Framework CLI

🐒 **MONKEY** es una herramienta de línea de comandos (CLI) para realizar tareas OSINT y escaneo de puertos, diseñada para ayudar a detectar actividades sospechosas y realizar análisis básicos de red de forma sencilla y rápida.

---

## Características principales

- Escaneo de puertos con identificación básica de servicios comunes (SSH, HTTP, FTP, Telnet...)
- Consulta WHOIS para dominios
- Búsqueda de subdominios
- Ping a hosts o dominios
- Análisis de cabeceras HTTP
- Interfaz interactiva con comandos y menús

---

## Advertencia ética

Este software es **solo para uso educativo y pruebas en entornos controlados**. No uses MONKEY para actividades ilegales o sin permiso explícito. El autor no se responsabiliza del mal uso.

---

## Requisitos

- Python 3.7 o superior
- Módulos: `requests`, `python-whois`

Puedes instalar los requisitos con:

```bash
pip install -r requirements.txt
Instalación y uso
Clona este repositorio:

git clone https://github.com/katalicism/MONKEY-Framework-CLI.git
cd MONKEY-Framework-CLI

Instala las dependencias:
pip install -r requirements.txt

Ejecuta la herramienta:

python monkey_terminal.py
