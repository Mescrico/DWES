# Añade a Producto un método vender(unidades) que reste stock y lance ValueError("Stock insuficiente") 
# si no hay suficiente. Provoca el error y captúralo en el programa principal.

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def __str__(self):
        return f"{self.nombre}: {self.precio}€ - {self.stock} stock"
    def __repr__(self):
        return f"Producto(nombre: {self.nombre}, precio: {self.precio}, stock: {self.stock})"
    def vender(self, unidades):
        if unidades > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock = self.stock - unidades 
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

p1 = Producto("Teclado Mecánico", 45.50, 5)

p1.vender(7)