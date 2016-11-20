import math
from datetime import datetime
import json

class Ejercicio0016:
    """Esta es la clase del ejercicio 16"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.base = data['base']
        self.potencia = data['potencia']
        self.maximo = 0
        self.diccionario = {}

    def calculaValor(self, salida):
        temporal = 1
        for x in range(1, self.potencia + 1):
            temporal *= self.base
        suma = 0
        for x in list(str(temporal)):
            suma += int(x)
        data = {"Suma": suma, "Numero": temporal}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))

retorno = Ejercicio0016('./data.json').calculaValor('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(value))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))