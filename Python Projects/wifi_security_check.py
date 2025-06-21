import os

#Aqui verificamos que la conexión es segura o no 

def check_wifi_security():
    try:
        result = os.popen("netsh wlan show interfaces").read()
        if "WPA2" in result or "WPA3" in result:
            print("Tu conexión Wi-Fi usa un protocolo seguro (WPA2/WPA3).")
        else:
            print("Cuidado: Tu conexión Wi-Fi no es segura.")
    except Exception as e:
        print(f"Error al verificar la seguridad de la conexión: {e}")

#Comprobamos que puertos quedan abiertos en la conexión

def check_open_ports():
    try:
        result = os.popen("netstat -an").read()
        print("\nPuertos abiertos encontrados:")
        for line in result.splitlines():
            if "LISTEN" in line:
                print(line)
    except Exception as e:
        print(f"Error al verificar puertos abiertos: {e}")

#Inicio

def main():
    print("Verificando seguridad de la conexión Wi-Fi...")
    check_wifi_security()
    
    print("\nAnalizando puertos abiertos...")
    check_open_ports()

if __name__ == "__main__":
    main()
    
#Permite a un archivo que se ejecute como un programa independiente o se importe como un modulo en otro script sin ejecutar el codigo automaticamente    