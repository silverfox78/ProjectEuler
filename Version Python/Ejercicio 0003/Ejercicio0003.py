# Clase de ejercicio 0003

import json
from pprint import pprint
class Ejercicio0003:
    """Esta es la clase del ejercicio 3"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.numeroevaluar = data['numeroevaluar']
        self.resto = self.numeroevaluar
        self.listaprimos = []
        self.divisores = []

    def esPrimo(sefl, numero):
        for valor in range(2, numero):
            if numero % valor == 0:
                return False
        return True

    def buscaFactores(self, salida):
        while self.resto != 1:
            primomaximo = 1
            for valor in self.listaprimos:
                if primomaximo < valor:
                    primomaximo = valor
                if self.resto % valor == 0:
                    self.divisores.append(valor)
                    self.resto = self.resto / valor
        
            salir = False
            while not salir:
                primomaximo += 1
                if self.esPrimo(primomaximo):
                    self.listaprimos.append(primomaximo)
                    if self.resto % primomaximo == 0:
                        self.divisores.append(primomaximo)
                        self.resto = self.resto / primomaximo
                        salir = True
        
        data = {"Factores": self.divisores}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return self.divisores
    
    def determinaMayor(seft, arreglo):
        mayor = 0
        for valor in arreglo:
            if valor > mayor:
                mayor = valor
        return mayor

clase = Ejercicio0003('./data.json')
arreglo = clase.buscaFactores('./resultado.json')
valor = clase.determinaMayor(arreglo)

print("Los fatores son: " + str(arreglo))
print("El mayor factor es: " + str(format(valor, ',d')))