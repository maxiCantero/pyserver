"""
Carga un archivo para procesar envio de comandos automaticamente
Pasos a seguir en pruebas:
    Carga de archivo
    Lectura de linea por linea y guardado en una lista
    Posible respuesta
        Si la respuesta es correcta pasar a nueva linea
        Sino esperar x segundos y volver a enviar misma linea
    Al finalizar de recorrer la lista enviar mensaje de finalizado correctamente o de error
"""
linea = ">STD00000120000200<                       \n"

# print(aux)
def prog():
    lista_prog = []
    files="test.txt"
    archivo = open(files,"r")
    for elemento in archivo.readlines():
        aux = elemento.find("<")
        aux = elemento[0:aux+1]
        if aux != "":
            lista_prog.append(aux)
    return lista_prog


    
print(prog())