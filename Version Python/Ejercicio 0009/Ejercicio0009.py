import itertools
import json
from datetime import datetime
class Ejercicio0009:
    """Esta es la clase del ejercicio 9"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.numero = data['numero']

    def determinaArreglo(self, salida):
        contador = 0
        for elem in itertools.combinations(range(1, int(self.numero / 2)), 3):
            tmp = sorted(elem)
            contador += 1
            if tmp[0] + tmp[1] > tmp[2]:
                if sum(tmp) == self.numero:
                    if (elem[0] ** 2 + elem[1] ** 2) == elem[2] ** 2:
                        data = {"Lista": tmp, "Multiplo": tmp[0] * tmp[1] * tmp[2], "Intento": contador}
                        with open(salida, 'w') as outfile:
                            json.dump(data, outfile)
                        return data


inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))

retorno = Ejercicio0009('./data.json').determinaArreglo('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(value))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))