import socket
import threading
from tkinter import *
from tkinter import messagebox

# Lista para almacenar los puertos abiertos
open_ports = []

# Función que escanea un puerto
def scan_port(ip, port):
    global open_ports
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
                result_display.insert(END, f"Puerto {port} está abierto.\n")
    except Exception as e:
        print(f"Error al escanear el puerto {port}: {e}")

# Función para realizar el escaneo con hilos
def threaded_scan(ip, start_port, end_port):
    global open_ports
    open_ports = []  # Reiniciamos la lista de puertos abiertos
    threads = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Mostrar el resumen final
    messagebox.showinfo("Resumen del análisis", f"Puertos abiertos: {open_ports}")

# Función para iniciar el análisis cuando se hace clic en el botón
def start_scan():
    ip = ip_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())

    result_display.delete(1.0, END)  # Limpiar resultados anteriores
    threaded_scan(ip, start_port, end_port)

# Crear la interfaz gráfica
root = Tk()
root.title("Escáner de Puertos")
root.geometry("500x400")

# Etiquetas y campos de entrada
Label(root, text="Dirección IP:").pack(pady=5)
ip_entry = Entry(root)
ip_entry.pack(pady=5)

Label(root, text="Puerto inicial:").pack(pady=5)
start_port_entry = Entry(root)
start_port_entry.pack(pady=5)

Label(root, text="Puerto final:").pack(pady=5)
end_port_entry = Entry(root)
end_port_entry.pack(pady=5)

# Botón para iniciar el escaneo
start_button = Button(root, text="Iniciar Escaneo", command=start_scan)
start_button.pack(pady=10)

# Área para mostrar resultados
Label(root, text="Resultados del escaneo:").pack(pady=5)
result_display = Text(root, height=10, width=60)
result_display.pack(pady=10)

# Iniciar la aplicación
root.mainloop()