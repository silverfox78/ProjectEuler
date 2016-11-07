import math
from datetime import datetime
import json

class Ejercicio0007:
    """Esta es la clase del ejercicio 7"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.limite = data['limite']

    def esPrimo(self, numero, lista):
        raiz = math.ceil(math.sqrt(numero))
        for valor in lista:
            if valor <= raiz:
                if numero % valor == 0 and valor != 1:
                    return False
            else:
                break            
        return True

    def determinaPrimo(self, salida):
        seguir = True
        numero = 0
        contador = 0
        inicia = []

        while seguir:
            numero += 1
            if numero <= 3:
                contador += 1
                inicia.append(numero)
                continue

            if numero % 2 == 0:
                continue

            if self.esPrimo(numero, inicia):
                contador += 1
                inicia.append(numero)

            if contador == self.limite + 1:
                seguir = False
                data = {"Primo": numero}
                with open(salida, 'w') as outfile:
                    json.dump(data, outfile)
                return data

inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))

retorno = Ejercicio0007('./data.json').determinaPrimo('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(format(value, ',d')))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))

