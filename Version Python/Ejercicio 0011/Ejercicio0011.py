import math
from datetime import datetime
import json

class Ejercicio0011:
    """Esta es la clase del ejercicio 11"""

    def __init__(self, archivo):
        with open(archivo) as data_file:    
            data = json.load(data_file)
        self.matriz = data['matriz']
        self.ancho = len(self.matriz)
        self.largo = len(self.matriz[0])
        self.posx = 0
        self.posy = 0
        self.lista = []
        self.producto = 0
        self.direccion = ""

    def multiplicaVector(self, vector):
        retorno = 1
        for valor in [int(x) for x in vector]:
            retorno *= valor
        return retorno
    
    def determinaIzquiera(self, posicionx, posiciony):
        if posicionx <= self.ancho - 4:
            lista = list(self.matriz[posiciony])[posicionx: posicionx + 4]
            suma = self.multiplicaVector(lista)
            if(suma > self.producto):
                self.posx = posicionx
                self.posy = posiciony
                self.lista = lista
                self.producto = suma
                self.direccion = "Izquierda"

    def determinaAbajo(self, posicionx, posiciony):
        if posiciony <= self.largo - 4:
            lista = []
            lista.append(self.matriz[posiciony][posicionx])
            lista.append(self.matriz[posiciony + 1][posicionx])
            lista.append(self.matriz[posiciony + 2][posicionx])
            lista.append(self.matriz[posiciony + 3][posicionx])
            suma = self.multiplicaVector(lista)
            if(suma > self.producto):
                self.posx = posicionx
                self.posy = posiciony
                self.lista = lista
                self.producto = suma
                self.direccion = "Abajo"

    def determinaDiagonalInferior(self, posicionx, posiciony):
        if posiciony <= self.largo - 4 and posicionx <= self.ancho - 4:
            lista = []
            lista.append(self.matriz[posiciony][posicionx])
            lista.append(self.matriz[posiciony + 1][posicionx + 1])
            lista.append(self.matriz[posiciony + 2][posicionx + 2])
            lista.append(self.matriz[posiciony + 3][posicionx + 3])
            suma = self.multiplicaVector(lista)            
            if(suma > self.producto):
                self.posx = posicionx
                self.posy = posiciony
                self.lista = lista
                self.producto = suma
                self.direccion = "Diagonal Inferior"
    
    def determinaDiagonalSuperior(self, posicionx, posiciony):
        if posiciony >= 3 and posicionx <= self.ancho - 4:
            lista = []
            lista.append(self.matriz[posiciony - 3][posicionx + 3])
            lista.append(self.matriz[posiciony - 2][posicionx + 2])
            lista.append(self.matriz[posiciony - 1][posicionx + 1])
            lista.append(self.matriz[posiciony][posicionx])
            suma = self.multiplicaVector(lista)
            if(suma > self.producto):
                self.posx = posicionx
                self.posy = posiciony
                self.lista = lista
                self.producto = suma
                self.direccion = "Diagonal Superior"

    def calculaVectores(self, posicionx, posiciony):
        self.determinaIzquiera(posicionx, posiciony)
        self.determinaAbajo(posicionx, posiciony)
        self.determinaDiagonalInferior(posicionx, posiciony)
        self.determinaDiagonalSuperior(posicionx, posiciony)

    def procesaMatriz(self, salida):
        for posx in range(0, self.ancho):
            for posy in range(0, self.largo):
                self.calculaVectores(posx, posy)
        
        data = {"Producto": self.producto, "PosicionX": self.posx, "PosicionY": self.posy, "Lista": self.lista, "Direccion": self.direccion}
        with open(salida, 'w') as outfile:
            json.dump(data, outfile)
        return data

inicio = datetime.now()
print("Inicio del ejercicio: " + str(inicio.strftime('%Y-%m-%d %H:%M:%S')))

retorno = Ejercicio0011('./data.json').procesaMatriz('./resultado.json')

for key, value in sorted(retorno.items()):
    print (key + ": " + str(value))

termino = datetime.now()
print("Termino del ejercicio: " + str(termino.strftime('%Y-%m-%d %H:%M:%S')))
print("Tiempo usado: " + str((termino - inicio).total_seconds()))