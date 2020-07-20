#import "mi_modulo" as   

import panda as pd
import numpy as np
import jason 

def _f_protected():
    #Función que recibe 1 entero y devuelve True si el valor es mayor que 5, y False en caso contrario
    l1 = []
    funcion = lambda x : x >5
    for elem in range(16):
        l1.append(elem)
    return list(filter(funcion, l1))

filter_ = _f_protected()
print(filter_)

def _f_protected():
    #Función que recibe 1 entero y devuelve True si el valor es mayor que 5, y False en caso contrario
    funcion = lambda x: x > 5
    l1 = [x for x in range(16)]#list_comprehension
    l1_filtrada = list(filter(funcion, l1))
    return l1_filtrada

filter_ = _f_protected()
print(filter_)
    

def _f_protected():
    l1 = [x for x in range(16)]
    l1_filtrada = list(filter(lambda x: x >5, l1))
    return l1_filtrada

filter_ = _f_protected()
print(filter_)