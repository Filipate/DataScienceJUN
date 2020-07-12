# This file represents your module.
# Write the code...


"""
Limpiar caracteres y espacios de una lista desordenada. Para que una lista de cadenas sea uniforme
y esté lista para el análisis: eliminar espacios en blanco, eliminar símbolos de puntuación 
y estandarizar el uso apropiado de mayúsculas
"""
import re
def clean_strings(strings):
  
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result

"""
otra forma es hacer una lista de operanciones que se necesita para un particular conjunto de datos
(ver python for data analyses 2nd edition)
"""

def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result

"""
ordenar una colección de cadenas por el número de letras distintas en cada cadena:
"""
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']

#podemos pasar una función lambda para ordenar

strings.sort(key=lambda x: len(set(list(x))))

"""
Función lambda para cambiar valores en columnas. En este ejemplo para transformar 
un tipo ya existente de tipo string a float. 
"""

nombre_funcion = lambda x: float(x[1:]) #donde x[1:]es la posición donde queremos cambiar
nombre_variable.nombre_de_la_columna = nombre_variable.nombre_de_la_columna.apply(nombre_funcion)