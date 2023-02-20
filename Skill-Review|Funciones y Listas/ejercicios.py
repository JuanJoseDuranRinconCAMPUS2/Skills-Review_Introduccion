#Una empresa tiene 500 almacenes. Cada almacén debe
#reportar el nombre y 5 registros c/u, contiene el tipo de articulo
#y el número de unidades vendidas de ese artículo.

#Haga un programa en Python para determinar cuál fue el
#almacén que mas vendió, cual fue el articulo más vendido de
#ese almacén y cual el más vendido en general.

import operator

def Bienvenida ():
    print("------------------------Almacenes-------------------------")
    print("Hola!, Bienvenido al sistema de registro de almacenes de nuestra emprea")
    return()
Local1a= {
    "Computadores": [40],
    "Celulares": [15],
    "Tablets": [2],
    "Televisores": [20],
    "Radios": [12],
    }
Local2b = {
    "Computadores": [63],
    "Celulares": [43],
    "Tablets": [5],
    "Televisores": [24],
    "Radios": [32],
    }


Local1 = {
    "Computadores": 40,
    "Celulares": 15,
    "Tablets": 2,
    "Televisores": 20,
    "Radios": 12,
    }
Local2 = {
    "Computadores": 63,
    "Celulares": 43,
    "Tablets": 5,
    "Televisores": 24,
    "Radios": 32,
    }
TotalLocal = {}
Bienvenida()

def calculos():
    total1=0
    total2=0
    for i in Local1.values():
        total1 += i
    for i in Local2.values():
        total2 += i
    print("\n\t------------------------Soluciones-------------------------")
    if total2 > total1:
        print(f"Feliciades local2 lograste un numero de ventas mayor que la competencia!")
        Local2_sort = sorted(Local2.items(), key=operator.itemgetter(1), reverse=True)
        MaxV=Local2_sort[0]
        print("\n\t------------------------DATOS-------------------------")
        print(f"El objeto mas vendido del Local2 fueron los {MaxV[0]} con un numero de venta total en la tienda de {MaxV[1]}")

    else:
        print(f"Feliciades local1 lograste un numero de ventas mayor que la competencia!")
        Local1_sort = sorted(Local1.items(), key=operator.itemgetter(1), reverse=True)
        MaxV=Local1_sort[0]
        print("\n\t------------------------DATOS-------------------------")
        print(f"El objeto mas vendido del Local1 fueron los {MaxV[0]} con un numero de venta total en la tienda de {MaxV[1]}")

    for key, value in Local1a.items():
        sum_array = [(Local1a[key][i] + Local2b[key][i]) for i, ele in enumerate(value)]
        TotalLocal.setdefault(key, sum_array)
        objeto = list(TotalLocal.keys())
        Numero = list(TotalLocal.values())
    print(f"El articulo mas vendido de los dos locales son los {objeto[0]} con un numero de ventas de {Numero[0]}")

calculos()
