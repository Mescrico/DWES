# Construye un catálogo a partir de una lista de filas (["Mochila,18.9,3", "Lápiz,0.8,100", "Cuaderno,2.5,12"]) 
# usando un bucle y el classmethod desde_fila. 
# Muestra cada producto con print y comprueba que todos son isinstance de Producto.

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
    @classmethod
    def desde_fila(cls, fila):
        nombre, precio, stock = fila.split(",")
        return cls(nombre, float(precio), int(stock))

filas = ["Mochila,18.9,3", "Lápiz,0.8,100", "Cuaderno,2.5,12"]

catalogo = []

for fila in filas:
    catalogo.append(Producto.desde_fila(fila))

print(catalogo)