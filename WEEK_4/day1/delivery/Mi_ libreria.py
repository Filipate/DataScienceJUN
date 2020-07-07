#import "mi_libreria" as   

  """
  limpiar caracteres y espacios de una lista desordenada. Para que una lista de cadenas sea uniforme
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