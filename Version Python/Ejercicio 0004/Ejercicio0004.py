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
        self.factores = []

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

# ranges = [(n, min(n+1, 10), n *min(n+1, 10)) for n in range(1, 10, 1)]
# print(ranges)

# it=iter(range(1000,100,-1))
# it1=iter(range(1000,100,-1))
# lst = [(next(it),next(it1)) for _ in range(10)]
# from operator import itemgetter
# listado = sorted(lst,key=lambda x: x[1], reverse=True)
# for key, value in listado:
#     #for key, value, producto in sorted(Ejercicio0004('./data.json').getLista().items()):
#     #print (key + ": " + str(format(value, ',d')) + " - Producto: " + str(format(producto, ',d')))
#     print (str(key) + ": " + str(value))


# lista = Ejercicio0004('./data.json').getLista()

# from operator import itemgetter
# listado = sorted(lista,key=lambda x: x[2], reverse=True)

# for key, value, producto in listado:
# #for key, value, producto in sorted(Ejercicio0004('./data.json').getLista().items()):
#     #print (key + ": " + str(format(value, ',d')) + " - Producto: " + str(format(producto, ',d')))
#     print (str(key) + ": " + str(value) + " - Producto: " + str(producto))
# #print(lista)

retorno = Ejercicio0004('./data.json').determinaPalindromo('./resultado.json')



for key, value in sorted(retorno.items()):
    print (key + ": " + str(format(value, ',d')))