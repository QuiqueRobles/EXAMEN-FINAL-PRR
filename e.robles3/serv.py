import socket, os, time, sys
import random

class Serv:

    def convertir_a_mayuscula(self,palabra):
        return palabra.upper()


    def obtener_puerto(self):
        puerto = 16000 + 10 * 1 + 3
        return puerto

    def contar_numero_lineas(self):
        path_fichero = "/home/user/Escritorio/e.robles3/prueba.txt"
        f=open(path_fichero,'r')
        n=len(f.readlines())
        f.close()
        return n

    def contar_numero_frases(self):
        path_fichero = "/home/user/Escritorio/e.robles3/prueba.txt"
        f = open(path_fichero, 'r')
        texto=f.read()
        n=len(texto.split('.'))
        f.close()
        return n-1

    def devolver_frase_aleatoria(self):
        path_fichero = "/home/user/Escritorio/e.robles3/prueba.txt"
        f=open(path_fichero,'r')
        frase=random.choice(f.read().split('.'))
        return frase

    def comprobar_frase(self,frase):
        if frase=="FRASE":
            i=1
        elif frase=="TOTAL":
            i=1
        else:
            i=0
        return i

    def servir(self):
        puerto= self.obtener_puerto()
        host="localhost"
        direccion = (host, puerto)
        socketPrincipal = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        socketPrincipal.bind(direccion)
        socketPrincipal.listen(1)
        while True:
            socketCliente, direccionCliente = socketPrincipal.accept()
            print("conexión establecida con el cliente "+ str(direccionCliente),file=sys.stderr)
            datos = socketCliente.recv(1024)
            datosDecod = datos.decode("utf8")
            self.comprobar_frase(datosDecod)
            datosDecodMayusculas=self.convertir_a_mayuscula(datosDecod)
            if datosDecodMayusculas == "FRASE":
                frase=self.devolver_frase_aleatoria()
                print("Se ha devuelto la frase "+ frase + " al cliente " + str(direccionCliente), file=sys.stderr)
                socketCliente.send(frase.encode("utf8"))
                socketCliente.close()
            elif datosDecodMayusculas == "TOTAL":
                numeroFrases = self.contar_numero_frases()
                numeroLineas = self.contar_numero_lineas()
                print("Se ha devuelto el numero de frases " + str(numeroFrases) + " y el numero de lineas " + str(numeroLineas) +"al cliente " + str(direccionCliente), file=sys.stderr)
                frase= str(numeroFrases) + " FRASES  " + str(numeroLineas) + "LINEAS"
                socketCliente.send(str(frase).encode("utf8"))
                socketCliente.close()
            else:
                fraseError="El servidor de Quique dice que introduzcas una frase válida"
                socketCliente.send(fraseError.encode("utf8"))
                socketCliente.close()


if __name__=="__main__":
    servidor = Serv()
    servidor.servir()

