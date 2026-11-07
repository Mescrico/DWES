# Predice el tipo de excepción de cada expresión antes de probarla en el intérprete: 
# int("3.5"), [1, 2][5], {}["x"], "a" + 1, 1 / 0, float("1,5") (esta última tiene trampa: pensad en el separador decimal).

# int("3.5") # ValueError por conversión imposible
# [1, 2][5] # IndexError por indice fuera de rango
# {}["x"] # KeyError por clave inexistente en un diccionario
# "a" + 1 # TypeError por operacion entre tipos incompatibles
# 1 / 0 # ZeroDivisionError por división entre 0
# float("1,5") # ValueError porque tiene como separador una , en vez de un .