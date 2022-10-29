# V1.0
import re
import socket
import threading
import time

global UDP_IP_CLIENT
global UDP_PORT_CLIENT
import unicodedata
from checksum import calculaCheckSum
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


def procesar_dato_gx7(buff):
    data = buff.split(";")
    # >SAK;ID=KX93;#000C; 25
    if len(data) > 2:
        ack = ">SAK;{};{};*".format(data[1], data[2])
        check = calculaCheckSum(ack)
        ack = ack + check[2:].upper() + "<"
        print(ack)
        return ack
    else:
        return data


def log(dato):
    x = datetime.now()
    fecha = x.strftime("%d%m%Y")
    fic = open("log_" + fecha + ".txt", "a")
    fic.writelines(str(x) + " " + dato + "\n")
    fic.close()


def thread_terminal():
    x = datetime.now()
    fecha = str(x.strftime("%d%m%Y"))
    global client_addr
    global sock
    # hostname = ""
    # portno = 7000
    # # portno=7500
    # sock.bind(('',portno))
    try:
        msg, client_addr1 = sock.recvfrom(1024)

        msg = str(msg)

        # if re.search(">RPI|>RPU|>RKO|>RID|>RAU", msg):
        if re.search(">R", msg):
            client_addr = client_addr1
            print("Mensaje recibido del cliente: ")
            print(msg)
            # acá va el llamado al archivo
            datos = msg.split(";")
            log(msg)
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


def envio_comando():
    try:
        # sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        msg = input()
        if client_addr != "":
            msg_out = msg.encode()
            sock.sendto(msg_out, client_addr)
    except:
        pass


arrancar_terminal = threading.Thread(target=thread_terminal)
envio = threading.Thread(target=envio_comando)
print("Terminal MCRWEB")
arrancar_terminal.start()
envio.start()
while True:
    if not arrancar_terminal.is_alive():
        try:
            arrancar_terminal = threading.Thread(target=thread_terminal)
            arrancar_terminal.start()
        except Exception:
            print(Exception())
    if not envio.is_alive():
        envio = threading.Thread(target=envio_comando)
        envio.start()
