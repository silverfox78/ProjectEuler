import math
from datetime import datetime
import json

class Ejercicio0015:
    """Esta es la clase del ejercicio 15"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.tope = data['tope']
        self.maximo = 0
        self.diccionario = {}

    def caminos(self, posicionx, posiciony, largo):
        valor = 0
        key = str(posicionx) + "_" + str(posiciony)
        if posicionx == 0 and posiciony == 0:
            return 1
        	
        if key in self.diccionario:
            return self.diccionario[key]
        if posicionx > 0:
            valor += self.caminos(posicionx - 1, posiciony, largo)
        if posiciony > 0:
            valor += self.caminos(posicionx, posiciony - 1, largo)

        self.diccionario[key] = valor
        return valor

    def tamannoCuadrado(self, largo):
        return self.caminos(largo, largo, largo)

    def procesaBusqueda(self, salida):
        for x in range(1, 21):
            self.maximo = self.tamannoCuadrado(x)
        data = {"Tamaño": self.tope, "Caminos": self.maximo}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))

retorno = Ejercicio0015('./data.json').procesaBusqueda('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(value))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))