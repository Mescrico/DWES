lista = ["Cuaderno", "Lapiz", "Mochila"]

acumulador = 0
for indice, producto in enumerate(lista, start=1):
    acumulador += 1
    print(f"Indice: {indice} - Producto: {producto}")
print(f"Total articulos: {acumulador}")