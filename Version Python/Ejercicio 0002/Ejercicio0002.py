# Clase de ejercicio 0002

import json
from pprint import pprint
class Ejercicio0002:
    """Esta es la clase del ejercicio 2"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.inicio = data['inicio']
        self.actual = data['actual']
        self.limite = data['limite']

    def getSuma(self, salida):
        suma = 0
        total = self.inicio + self.actual
        while self.actual < self.limite:
            suma = self.inicio + self.actual
            self.inicio = self.actual
            self.actual = suma
            #print("inicio: " + str(self.inicio) + " - actual: " + str(self.actual) + " - suma: " + str(suma))
            if suma % 2 == 0:
                total += suma;
        data = {"Total": total}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

retorno = Ejercicio0002('./data.json').getSuma('./resultado.json')

for key, value in retorno.items():
    print (key + ": " + str(format(value, ',d')))