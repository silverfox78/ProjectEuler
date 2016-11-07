import itertools
import json
from datetime import datetime
from pprint import pprint
from time import gmtime, strftime

class Ejercicio0005:
    """Esta es la clase del ejercicio 5"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.inicio = data['inicio']
        self.fin = data['fin']

    def esPrimo(self, numero):
        for valor in range(2, numero):
            if numero % valor == 0:
                return False
        return True

    def getListaPrimos(self):
        primos = []
        for valor in range(self.inicio, self.fin + 1):
            if self.esPrimo(valor):
                primos.append(valor)
        return list(primos)

    def getArreglo(self):
        return [x for x in range(self.inicio, self.fin + 1, 1)]
        
    def getListaCombinada(self, lista):
        retorno = []
        for tmp in range(0, len(lista) + 1):
            for elem in itertools.combinations(lista, tmp):
                retorno.append(elem)
        return list(retorno)

    def getListaNumero(self, lista):
        retorno = []
        for item in lista:
            valor = 1
            if len(item) > 0:
                for numero in item:
                    valor *= numero
            retorno.append(valor)
        return retorno

    def esCorrecto(self, numero, primos):
        for divisor in primos:
            if numero % divisor != 0:
                return False
        return True

    def determinaMinimoMultiplo(self, salida):
        primos = self.getListaPrimos()
        arreglo = self.getArreglo()
        combinados = self.getListaCombinada(arreglo)
        numeros = sorted(list(set(self.getListaNumero(combinados))))
        retorno = 0
        for numero in numeros:
            if self.esCorrecto(numero, arreglo):
                retorno = numero
                break

        data = {"Numero": retorno}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))
retorno = Ejercicio0005('./data.json').determinaMinimoMultiplo('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(format(value, ',d')))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))
