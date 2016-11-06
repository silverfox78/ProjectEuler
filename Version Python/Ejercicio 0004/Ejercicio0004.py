# Clase de ejercicio 0004

import json
from pprint import pprint
class Ejercicio0004:
    """Esta es la clase del ejercicio 4"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.inicio = data['inicio']
        self.fin = data['fin']
        self.factores = []
        self.palindromo = 0

    def esPalindromo(self, numero):
        lista = list(str(numero))
        if lista == [lista[i-1] for i in range(len(lista),0,-1)]:
            return True
        return False

    def determinaPalindromo(self, salida):
        for multiplicando in range(self.inicio, self.fin):
            for multiplicador in range(multiplicando, self.fin):
                numero = multiplicando * multiplicador
                if self.esPalindromo(numero) and (numero > self.palindromo):
                    self.palindromo = numero
                    data = {"Palindromo": self.palindromo, "Multiplicando": multiplicando, "Multiplicador": multiplicador}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

retorno = Ejercicio0004('./data.json').determinaPalindromo('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(format(value, ',d')))