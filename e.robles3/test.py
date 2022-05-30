import unittest

from serv import Serv

class TestServidor(unittest.TestCase):

    def test_mayusculas(self):
        servidor=Serv()
        palabra="fiChEro"
        texto_mayusculas=servidor.convertir_a_mayuscula(palabra)
        self.assertEqual("FICHERO",texto_mayusculas)

    def test_devolver_puerto(self):
        servidor = Serv()
        puerto=16013
        puertoServ = servidor.obtener_puerto()
        self.assertEqual(puerto, puertoServ)

    def test_contar_lineas_fichero(self):
        servidor = Serv()
        numero_lineas=servidor.contar_numero_lineas()
        self.assertEqual(numero_lineas,4)

    def test_contar_frases_fichero(self):
        servidor = Serv()
        numero_lineas=servidor.contar_numero_frases()
        self.assertEqual(numero_lineas,5)

    def test_frase_aleatoria(self):
        servidor = Serv()
        frase = servidor.devolver_frase_aleatoria()
        self.assertTrue(isinstance(frase,str))

    def test_mensaje_erroneo_cliente(self):
        servidor = Serv()
        frase="Tocame el pito"
        verdadero_falso = servidor.comprobar_frase(frase)
        self.assertEqual(verdadero_falso,0)


    # def test_devolver_frase(self):
    #     servidor=Qserv()
    #     numeroLetras=servidor.contarLetra("palabra","a")
    #     print(numeroLetras)
    #     self.assertEqual(numeroLetras,3)