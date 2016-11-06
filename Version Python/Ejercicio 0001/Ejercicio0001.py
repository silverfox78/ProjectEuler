# Clase de ejercicio 0001

import json
from pprint import pprint
class Ejercicio0001:    
    """Esta es la clase del ejercicio 1"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.iniciorango = data['inicio']
        self.finrango = data['termino']
        self.listamultiplos = data['multiplos']
        
    def getTotal(self, salida):
        """Esta funcion es la ejecuta el calculo"""
        total = 0
        contador = 0
        
        for numeroEvaluar in range(self.iniciorango, self.finrango):
            sumo = False
            for multiplo in self.listamultiplos:
                if (numeroEvaluar % multiplo == 0) and (not sumo):
                    total += numeroEvaluar
                    contador += 1
                    sumo = True
        data = {'total': total, 'contador': contador}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

retorno = Ejercicio0001('./data.json').getTotal('./resultado.json')

print ("Total: " + str(retorno['total']) + "\nCantidad de multiplos: " + str(retorno['contador']))