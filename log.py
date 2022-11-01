from datetime import datetime
"""
Funcion para guardar en archivo (posibilidad de sacarla afuera)
"""

def log(dato):

    x = datetime.now()
    fecha = x.strftime("%d%m%Y")
    fic = open("log_" + fecha + ".txt", "a")
    fic.writelines(str(x) + " " + dato + "\n")
    fic.close()