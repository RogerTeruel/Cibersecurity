"""Paso 1: Importo el módulo del sistema para
   poder utilizar sys.exit() y salir del programa
"""
import sys
from tcp_scan import tcp_scan

# Paso 2: Aqui importare los modulos de escaneo
# from scanners.tcp_scan import run_tcp_scan
# from scanners.udp_scan import run_udp_scan  etc...  

"""Paso 3:Creo la función show_menu() 
que mostrará el menú"""
def show_menu():
    print(r"""
╔═════════════════════════════════════════════════════════════════════════════════════╗
║                ██████╗                                                              ║
║     █████╗     ██╔══██╗     █████╗                                                  ║
║     █████║     ██████╔╝     █████║                                                  ║
║     █████║     ██╔██╔╝      █████║                                                  ║
║     █████║     ██║ ██╗      █████║                                                  ║
║     █████║     ╚═╝ ╚═╝      █████║                                                  ║
║     █████║                  █████║     Made for Cybersecurity & Pentesting          ║
║     █████████████████████████████║     LinkedIn --> www.linkedin.com/in/roger-tm    ║
║     █████████████████████████████║     GitHub ----> github.com/RogerTeruel          ║
║     █████╔══════════════════█████║     Email -----> rodhammer.forge@proton.me       ║
║     █████║   Powered by:    █████║                                                  ║
║     █████║                  █████║                                                  ║
║     █████║ RodHammer.forge  █████║                                                  ║
║     █████║                  █████║                                                  ║
║     █████║                  █████║                                                  ║
║     ╚════╝                  ╚════╝                                                  ║
╚═════════════════════════════════════════════════════════════════════════════════════╝
""")
    print("\n" + "=" * 40)
    print("    RodHammer's Network Scanner Suite")
    print("=" * 40)
    print("1. Advanced TCP Scan")
    print("2. Advanced UDP Scan")
    print("3. Advanced OS Detector")
    print("4. Advanced SMTP Scan")
    print("5. Advanced Vulnerability Scan")
    print("6. All-in-One Scan")
    print("0. Exit")
    print("=" * 40)

"""Paso 4: Creo la función main() esta se ejecuta en bucle 
hasta que el usuario decida salir del programa."""

def run_tcp_scan():
    print("\n[ Advanced TCP Scan ]")
    ip = input("Target IP address: ").strip()
    try:
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))
        timeout = float(input("Timeout (e.g. 0.5): "))
        threads = int(input("Max threads (e.g. 100): "))
        print("\nScanning... Please wait.\n")
        results = tcp_scan(ip, start_port, end_port, timeout=timeout, max_threads=threads)

        print("=" * 50)
        print(f"{'PORT':<8}{'STATUS':<20}{'SERVICE'}")
        print("=" * 50)
        for port, status, service in results:
            print(f"{port:<8}{status:<20}{service}")
        print("=" * 50)

    except ValueError as ve:
        print(f"[!] Input Error: {ve}")
    except Exception as e:
        print(f"[!] Unexpected Error: {e}")

def main():
    while True: # Mientras sea verdadero
        
        show_menu() # Mostramos el menú 
       
        # Paso 5: Mientras visualizamos el menu
        # Solicito una opción al usuario
        choice = input("Choice an option: ")
        
        # Paso 6: Evaluo la opción elegida por el usuario
        if choice == "0": # Si el usuario elige 0
            print("\nThank you for using RodHammer's Network Scanner Suite")
            print("Exiting the program...")
            sys.exit(0) # Salimos del programa
       
        elif choice == "1": # Si el usuario elige 1
            print("·Executing TCP Scan...")
            # Aquí llamaremos a la función del TCP scan en el futuro
            # run_tcp_scan()
            print("TCP Scan completed.")
    
        elif choice == "2": # Si el usuario elige 2
            print("·Executing UDP Scan...")
            # run_udp_scan()
            print("UDP Scan completed.")

        elif choice == "3": # Si el usuario elige 3
            print("·Executing OS Detector...")
            # run_os_detector()
            print("OS Detection completed.")

        elif choice == "4": # Si el usuario elige 4
            print("·Executing SMTP Scan...")
            # run_smtp_scan()
            print("SMTP Scan completed.")

        elif choice == "5": # Si el usuario elige 5
            print("·Executing Vulnerability Scan...")
            # run_vuln_scan()
            print("Vulnerability Scan completed.")

        elif choice == "6":
            print("·Executing all scans in one...")
            # run_all_scans()
            print("All scans completed.")

        else: # Si el usuario elige una opción no válida
            print("Invalid option. Please check your selection.")

# Paso 5: Nos aseguramos de que el script se ejecute
if __name__ == "__main__":
    main()