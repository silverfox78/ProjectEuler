import math
from datetime import datetime
import json

class Ejercicio0017:
    """Esta es la clase del ejercicio 17"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.maximo = data['maximo']
        self.total = 0

    def numeroEnPalabra(self, numero):
        unidad = ['','one','two','three','four','five','six','seven','eight','nine']
        unidades = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', 'seventeen','eighteen','nineteen']
        decenas = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', 'eighty','ninety']
        if numero >= 1000: return 'onethousand'
        largo = len(str(numero))
        numerotexto = str(numero)
        retorno = []
        u = int(numerotexto[largo - 1])
        d = 0
        if numero >= 10: d = int(numerotexto[largo - 2])
        c = 0
        if numero >= 100: c = int(numerotexto[largo - 3])
        if c >= 1:
            retorno.append(unidad[c])
            retorno.append('hundred')
        
        if c >= 1 and numero % 100 != 0:
            retorno.append('and')
        
        if d>=1 and u == 0:
            retorno.append(decenas[d])
        else:
            if d < 1:
                retorno.append(unidad[u])
            elif d < 2:
                retorno.append(unidades[u])
            else:
                retorno.append(decenas[d])
                retorno.append(unidad[u])
        return ''.join(retorno)

    def determinaLetras(self, salida):
        self.total = 0
        for x in range(1, self.maximo + 1):
            self.total += len(self.numeroEnPalabra(x))
        
        data = {"Total Letras": self.total}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))

retorno = Ejercicio0017('./data.json').determinaLetras('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(value))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))