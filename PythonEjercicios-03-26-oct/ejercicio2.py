numero = int(input("Escribe el numero para su tabla de multiplicar: "))

for linea in range(1,11):
    print(f"{numero} x {linea} = {numero*linea}")