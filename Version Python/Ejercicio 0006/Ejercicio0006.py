import json

class Ejercicio0006:
    """Esta es la clase del ejercicio 6"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.inicio = data['inicio']
        self.fin = data['fin']

    def getValores(self):
        suma = 0
        potencia = 0
        for valor in range(self.inicio, self.fin + 1, 1):
            suma += valor
            potencia += valor ** 2
        return {"suma": suma, "potencia": potencia}
    
    def determinaDiferecia(self, salida):
        valores = self.getValores()
        data = {"suma": valores['suma'] ** 2, "potencia": valores['potencia'], "diferencia": (valores['suma'] ** 2) - valores['potencia']}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

retorno = Ejercicio0006('./data.json').determinaDiferecia('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(format(value, ',d')))