import math
from datetime import datetime
import json

class Ejercicio0013:
    """Esta es la clase del ejercicio 13"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.numeros = data['lista']
        self.arreglosuma = []
        self.arreglotmp = []

    def VectorTexto(seft, vector):
        largo = len(vector)
        retorno = ""
        if largo > 0:
            for x in range(0, largo):
                retorno += "%s" %(vector[x])
        return retorno

    def SumaVector(self, vector):
        self.arreglotmp = []
        largo = len(self.arreglosuma)
        resto = 0
        if largo <= 0:
            self.arreglosuma = vector
        else:
            largovector = len(vector)
            largoacomulado = len(self.VectorTexto(self.arreglosuma))
            largo = 0
            diferencia = 0
            if largoacomulado > largovector:
                largo = largoacomulado
                diferencia = largoacomulado - largovector  
            else:
                largo = largovector

            for x in range(largo - 1, 0-1, -1):
                if x - diferencia >= 0:
                    suma = int(vector[x - diferencia]) + int(self.arreglosuma[x]) + resto
                else:
                    suma = int(self.arreglosuma[x]) + resto
                if suma >= 10:
                    resto = 1
                    suma = suma - 10
                else:
                    resto = 0
                self.arreglotmp.append(suma)
            if resto > 0:
                self.arreglotmp.append(resto)
            self.arreglosuma = [self.arreglotmp[i-1] for i in range(len(self.arreglotmp),0,-1)]
            
        return str(self.VectorTexto(self.arreglosuma))

    def ProcesarSumas(self, salida):
        largo = len(self.numeros)
        sumafinal = ""
        for x in range(0, largo):
            sumafinal = self.SumaVector(self.numeros[x])
        data = {"Suma": sumafinal, "DiezElemento": str(self.VectorTexto(list(sumafinal)[0:10]))}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))

retorno = Ejercicio0013('./data.json').ProcesarSumas('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(value))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))