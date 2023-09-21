def verifica_primo(nro):
    es_primo = True  
    for i in range(2, nro):  
        if nro % i == 0: 
            es_primo = False  
            break 
    return es_primo 


def valor_modal(lista):
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repeticiones[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repeticiones.append(1)
    moda = lista_unicos[0]
    maximo = lista_repeticiones[0]
    for i, elemento in enumerate(lista_unicos):
        if lista_repeticiones[i] > maximo:
            moda = lista_unicos[i]
            maximo = lista_repeticiones[i]
    return moda, maximo


def conversion_grados(valor, origen, destino):
    if origen == 'celsius':
        if destino == 'celsius':
            valor_destino = valor  
        elif destino == 'farenheit':
            valor_destino = (valor * 9 / 5) + 32 
        elif destino == 'kelvin':
            valor_destino = valor + 273.15 
        else:
            print('Parámetro de Destino incorrecto') 
    elif origen == 'farenheit':
        if destino == 'celsius':
            valor_destino = (valor - 32) * 5 / 9
        elif destino == 'farenheit':
            valor_destino = valor 
        elif destino == 'kelvin':
            valor_destino = ((valor - 32) * 5 / 9) + 273.15  
        else:
            print('Parámetro de Destino incorrecto') 
    elif origen == 'kelvin':
        if destino == 'celsius':
            valor_destino = valor - 273.15  
        elif destino == 'farenheit':
            valor_destino = ((valor - 273.15) * 9 / 5) + 32  
        elif destino == 'kelvin':
            valor_destino = valor  
        else:
            print('Parámetro de Destino incorrecto')  
    else:
        print('Parámetro de Origen incorrecto') 
    
    return valor_destino 


def factorial (a):
    if type (a) != int:
        a = int (a)
    if a < 0:
        Resultado = 'Para este número no se puede calcular factorial'
    elif a > 1:
        Resultado = a * factorial (a - 1)
    else:
        Resultado = 1
    return Resultado

class Dtodito:
    
    def __init__ (self, lista):
        self.lista = lista

    def Primo (self):
        for i in self.lista:
            if verifica_primo(i) == True:
                print (f'{i} es primo')
            else:
                print (f'{i} no es primo')

    def mas_alto (self):
        print (valor_modal(self.lista))

    def temp (self, origen, destino):
        for i in self.lista:
            print (f'{i} grados {origen} son {conversion_grados(i, origen, destino)} {destino}')

    def Factorial (self):
        for i in self.lista:
            print (factorial(i))