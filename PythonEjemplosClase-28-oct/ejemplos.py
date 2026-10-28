import mates
# Funciones def
print("Funciones def")
def saludar(nombre, mensaje="mensaje predeterminado"):
    print(f"Hola {nombre}, {mensaje}")

saludar("mario", "que tal")
saludar("mario")

print("--------------")
# Lambdas
print("Lambdas")

productos = [
    
{"nombre": "Mochila", "precio": 18.9},
    
{"nombre": "Cuaderno", "precio": 2.5},
    
{"nombre": "Lápiz", "precio": 0.8},
]

ordenados = sorted(productos, key=lambda p: p["precio"])

print(ordenados)

print("--------------")
# sqrt importado
print("SQRT importado")

print(mates.sqrt(5))