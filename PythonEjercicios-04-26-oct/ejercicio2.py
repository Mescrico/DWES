dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]
print("Primeros dos dias")
print(dias[:2])
print("Ultimos dos dias")
print(dias[-2:])
print("Dias pares con paso 2")
print(dias[1::2])
copia = dias[:]
copia.append("Sabado")
print("Copia")
print(copia)
print("Original")
print(dias)
