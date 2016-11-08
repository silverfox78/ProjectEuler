import math
from datetime import datetime
import json

class Ejercicio0010:
    """Esta es la clase del ejercicio 10"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.tope = data['numero']

    def esPrimo(self, numero, lista):
        raiz = math.ceil(math.sqrt(numero))
        for valor in lista:
            if valor <= raiz:
                if numero % valor == 0 and valor != 1:
                    return False
            else:
                break
        return True

    def determinaSumaPrimos(self, salida):
        seguir = True
        numero = 1
        contador = 0
        suma = 0
        ultimoprimo = 0
        inicia = []

        while seguir:
            numero += 1
            if numero <= 3:
                contador += 1
                suma += numero
                ultimoprimo = numero
                inicia.append(numero)
                continue

            if numero >= self.tope:
                seguir = False
                break
            else:
                if numero % 2 == 0:
                    continue

                if numero > 10:
                    if numero % 3 == 0:
                        continue
                    
                    if numero % 5 == 0:
                        continue

                    if numero % 7 == 0:
                        continue

                if self.esPrimo(numero, inicia):
                    contador += 1
                    suma += numero
                    ultimoprimo = numero
                    inicia.append(numero)

        data = {"UltimoPrimo": ultimoprimo, "Suma": suma}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))

retorno = Ejercicio0010('./data.json').determinaSumaPrimos('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(value))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))