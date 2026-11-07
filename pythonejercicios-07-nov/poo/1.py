# Crea la clase LineaPedido con atributos producto (un Producto) y unidades, y un método subtotal() que use producto.precio. 
# Construye un pedido con tres líneas y calcula el total recorriéndolas con un acumulador. Añade __str__ y __repr__ a ambas clases 
# y comprueba cuál se usa en cada caso (print frente a intérprete).

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"{self.nombre}: {self.precio}€"
    def __repr__(self):
        return f"Producto(nombre: {self.nombre}, precio: {self.precio})"
class LineaPedido:
    def __init__(self, producto, unidades):
        self.producto = producto
        self.unidades = unidades
    def subtotal(self):
        total = self.unidades*self.producto.precio
        return total
    def __str__(self):
        return f"{self.producto} - {self.unidades} uds"
    def __repr__(self):
        return f"LineaPedido(producto: {self.producto}, unidades: {self.unidades})"
    
p1 = Producto("Teclado Mecánico", 45.50)
p2 = Producto("Ratón Gaming", 25.00)
p3 = Producto("Alfombrilla XXL", 15.20)

lineas = [
    LineaPedido(p1, 1),
    LineaPedido(p2, 2),
    LineaPedido(p3, 1)
]

total = 0
for linea in lineas:
    print(linea)
    total += linea.subtotal()
print(f"Total: {total:.2f}€")

