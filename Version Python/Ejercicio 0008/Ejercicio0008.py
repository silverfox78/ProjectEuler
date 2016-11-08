import math
from datetime import datetime
import json

class Ejercicio0008:
    """Esta es la clase del ejercicio 8"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.numero = data['numero']
        self.maximo = 0
        self.lista = []
        self.posicion = 0

    def Multiplicar(self, lista):
        retorno = 1
        for i in lista:
            retorno *= int(i)
        return retorno

    def generaArreglos(self, salida):
        lista = []
        for i in range(0, len(list(str(self.numero))) - 13):
            posiciontmp = i
            listatmp = list(str(self.numero))[posiciontmp:posiciontmp+13]
            suma = self.Multiplicar(listatmp)
            if suma > self.maximo:
                self.maximo = suma
                self.posicion = posiciontmp
                self.lista = listatmp

        data = {"Maximo": self.maximo, "Lista": self.lista, "Posicion": self.posicion}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))

retorno = Ejercicio0008('./data.json').generaArreglos('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(value))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))