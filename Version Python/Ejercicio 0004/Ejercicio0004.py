# Clase de ejercicio 0004

import json
from pprint import pprint
class Ejercicio0004:
    """Esta es la clase del ejercicio 4"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.inicio = data['inicio']
        self.fin = data['fin'] - 1

    def esPalindromo(self, numero):
        lista = list(str(numero))
        if lista == [lista[i-1] for i in range(len(lista),0,-1)]:
            return True
        return False

    def getLista(self):
        listapares = []
        for multiplicando in range(self.fin, self.inicio, -1):
            for multiplicador in range(multiplicando, self.inicio, -1):
                listapares.append((multiplicando, multiplicador, multiplicando * multiplicador))
        return list(listapares)

    def determinaPalindromo(self, salida):
        from operator import itemgetter
        listado = sorted(self.getLista(), key=lambda x: x[2], reverse=True)
        for key, value, producto in listado:
            if self.esPalindromo(producto):
                data = {"Palindromo": producto, "Multiplicando": key, "Multiplicador": value}
                with open(salida, 'w') as outfile:
                    json.dump(data, outfile)
                return data

retorno = Ejercicio0004('./data.json').determinaPalindromo('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(format(value, ',d')))