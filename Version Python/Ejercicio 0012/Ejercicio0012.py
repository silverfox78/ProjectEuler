import math
from datetime import datetime
import json

class Ejercicio0012:
    """Esta es la clase del ejercicio 12"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.tope = data['tope']
        self.primomaximo = 0
        self.primos = []

    def esPrimo(self, evaluar):
        if evaluar <= 1:
            return False
        raiz = math.ceil(math.sqrt(evaluar))
        for valor in self.primos:
            if valor <= raiz:
                if evaluar % valor == 0 and valor != 1:
                    return False
            else:
                break
        self.primomaximo = evaluar
        self.primos.append(self.primomaximo)
        return True
    
    def analizaDivisores(self, lista):
        listatmp = sorted(list(set(lista)))
        total = 1
        for x in listatmp:
            total *= lista.count(x) + 1
        return total

    def getDivisores(self, numeroevaluar):
        resto = numeroevaluar
        listadivisores = []
        while resto > 1:
            tmp = resto
            for x in self.primos:
                if resto % x == 0:
                    resto = resto / x
                    listadivisores.append(x)
            if resto == tmp:
                cont = self.primomaximo + 1
                while not self.esPrimo(cont):
                    cont += 1
        return self.analizaDivisores(listadivisores)

    def ProcesaBusqueda(self, salida):
        numero = 0
        mayor = 0
        mayorcantidad = 0
        procesar = True
        secuencia = 0
        while procesar:
            secuencia += 1
            numero += secuencia
            cantidad = self.getDivisores(numero)
            if cantidad > mayorcantidad:
                mayorcantidad = cantidad
                mayor = numero
            if mayorcantidad >= self.tope:
                procesar = False

        data = {"NumeroMayor": mayor, "Cantidad": mayorcantidad}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))

retorno = Ejercicio0012('./data.json').ProcesaBusqueda('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(value))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))