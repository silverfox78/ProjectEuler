import math
from datetime import datetime
import json
from bisect import bisect_left, insort_left

class Ejercicio0014:
    """Esta es la clase del ejercicio 14"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.inicio = data['inicio']
        self.arreglo = [(1,1)]
        self.maximo = 0
    
    def bi_contains(lst, item):
        """ efficient `item in lst` for sorted lists """
        # if item is larger than the last its not in the list, but the bisect would 
        # find `len(lst)` as the index to insert, so check that first. Else, if the 
        # item is in the list then it has to be at index bisect_left(lst, item)
        return (item <= lst[-1]) and (lst[bisect_left(lst, item)] == item)

    def buscaValor(self, numero):
        lista = [y for x, y in list(self.arreglo) if x == numero]
        #print(lista)
        if len(lista) > 0: 
            return lista[0]
        return 0

    def recursivo(self, numero, contador):
        if numero == 1:
            return contador + 1
        # tmp = self.buscaValor(numero)
        # if tmp > 0:
        #     return contador + tmp
        if numero % 2 == 0:
            return self.recursivo(int(numero / 2), contador + 1)
        else:
            return self.recursivo((3 * numero) + 1, contador + 1)

    def procesaNumero(self, salida):
        valor = 0
        for x in range(1, self.inicio + 1):
            #print(self.arreglo)
            valor = int(str(self.recursivo(x, 0)))
            # tmp = self.buscaValor(x)
            # if tmp <= 0:
            #     self.arreglo.append((x, valor))
            if self.maximo < valor:
                self.maximo = valor
                print("Numero: " + str(x) + " - Valor: " + str(self.maximo)) #+ " - Largo: " + str(len(self.arreglo)))
                data = {"NumeroMayor": x, "Cantidad": self.maximo}
                with open(salida, 'w') as outfile:
                    json.dump(data, outfile)
        return data


inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))

retorno = Ejercicio0014('./data.json').procesaNumero('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(value))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))