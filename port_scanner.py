import socket
#Uso la libreria socket para establecer conexiones de red

def scan_port(ip, port):
    #Escaneamos un puerto en una direccion IP, verificara si esta abierta o no
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        #Establezco el tiempo de espera en 1 segundo
        result = sock.connect_ex((ip, port))
        #Intenta conectarse al puerto en la IP mencionada
        if result == 0:
            print(f"El Puerto {port} en {ip} esta abierta.")
        else:
            print(f"El puerto {port} en {ip} esta cerrado") 
#Aqui establecemos que imprima en el caso de que este abierto el puerto o no
def main():
    ip = input("Ingresar la direccion IP a escanear: ")
    start_port = int(input("Ingresar el puerto inicial: "))
    end_port = int(input("Ingresa el puerto final: "))
#Aqui es donde ingresamos la IP y el rango de Puertos a analizar                  
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)
if __name__ == "__main__":
    main()
#Permite a un archivo que se ejecute como un programa independiente o se importe como un modulo en otro script sin ejecutar el codigo automaticamente    