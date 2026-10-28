nombre = str(input("Escribe el producto: "))
precio = float(input("Escribe el precio: "))
unidades = int(input("Escribe el stock: "))
disponible = bool(input("Disponible? True or False: "))

print(f"{nombre} | {precio:.2f} € - x{unidades} - {disponible}")