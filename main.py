# V1.0
import re
import socket
import threading
import time

global UDP_IP_CLIENT
global UDP_PORT_CLIENT
import unicodedata
from checksum import calculaCheckSum
from log import log
from archivo import prog
from datetime import datetime
import sys

# sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# print("socket creado")
# hostname = "127.0.0.1"
# portno = 7500
# sock.bind((hostname,portno))
# print("socket en direccion {}, y puerto numero {}".format(hostname,portno))
client_addr = []
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
hostname = ""
portno = 7000
# portno=7500
sock.bind(("", portno))


"""
Armado de ACK para GX7
"""
def procesar_dato_gx7(buff):
    data = buff.split(";")
    
    if len(data) > 2:
        ack = ">SAK;{};{};*".format(data[1], data[2])
        check = calculaCheckSum(ack)
        ack = ack + check[2:].upper() + "<"
        print(ack)
        return ack
    else:
        return data




# Funcion que recepciona datos y hace parser inicial
def thread_terminal():
    x = datetime.now()
    fecha = str(x.strftime("%d%m%Y"))
    global client_addr
    global sock
    
    try:
        msg, client_addr1 = sock.recvfrom(1024)
        msg = str(msg)

        if re.search(">R", msg):
            client_addr = client_addr1 
            print("Mensaje recibido del cliente: ")
            print(msg)  # Imprime en pantalla mensaje recibido del post remoto
            # acá va el llamado al archivo
            datos = msg.split(";")
            log(msg)
            # Si el dato es mayor a dos caracteres crea el ack
            if len(datos) > 2:
                datap = procesar_dato_gx7(msg)
                msg_out = datap.encode()
                sock.sendto(msg_out, client_addr)
            # sock.close()
        else:
            pass
            # sock.close()
    except:
        print(sys.exc_info())


# ENVIO DE COMANDOS POR TECLADO
def envio_comando():
    try:
        # sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        msg = input()
        if client_addr != "":
            msg_out = msg.encode()
            sock.sendto(msg_out, client_addr)
    except:
        pass


def envio_comando_archivo():
    try:
        lista_prog = prog()
        
        for elemento in lista_prog:
            
            if client_addr != "":
                msg_out = elemento.encode()
                sock.sendto(msg_out, client_addr)
    except:
        # print("error")
        pass

# MAIN
arrancar_terminal = threading.Thread(target=thread_terminal) # Hilo para recepcion de datos
envio = threading.Thread(target=envio_comando) # Hilo para envio de datos
print("Terminal MCRWEB") # Mensaje inicial
arrancar_terminal.start() # Arranca hilo terminal
envio.start() # Arranca hilo envio
flag_prog=True
while True: 
    # envio_comando_archivo()
    if not arrancar_terminal.is_alive():
        try:
            arrancar_terminal = threading.Thread(target=thread_terminal)
            arrancar_terminal.start()
        except Exception:
            print(Exception())
    if not envio.is_alive():
        if flag_prog:
            envio = threading.Thread(target=envio_comando)
            envio.start()
