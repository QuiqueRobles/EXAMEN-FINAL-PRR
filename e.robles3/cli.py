import socket
import time

def cli():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        print("\nBIENVENIDO A MI EXAMEN FINAL\n")
        direccion=input("Por favor introduzca la dirección: ")
        puerto=input("Por favor introduzca el puerto: ")
        s.connect((direccion, int(puerto)))
        print("\nSE HA CONECTADO USTED AL SERVIDOR\n\nPara que el servidor le devuelva una frase ponga FRASE")
        print("Para que el servidor le muestre el número de frases introduzca TOTAL")
        palabra = input("INPUT: ")
        s.send(palabra.strip().encode("utf8"))  # envia mensaje al cliente
        datosServ = s.recv(1024)
        datosServDecod = datosServ.decode("utf8")
        print(datosServDecod)
        s.close()
    except:
         print("Hubo un problemas con el servidor, vuelva a ejecutar el cliente")
         s.close()

cli()
cli()
cli()