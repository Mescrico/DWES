# Añade a Producto la propiedad de solo lectura total (el valor del stock: precio * stock) 
# y convierte stock en propiedad con setter que rechace valores negativos lanzando ValueError. 
# Comprueba que asignar un stock negativo falla y que mochila.total se calcula solo.

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

    @property
    def total(self):
        total = self.precio * self.stock
        return total

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        if stock < 0:
            raise ValueError("Stock no puede ser negativo")
        self._stock = stock

mochila = Producto("Mochila", 20.0, 5)
print(mochila)
print(f"Valor total de la mochila: {mochila.total} €")  # Se calcula automáticamente

try:
    mochila.stock = -67
except ValueError as e:
    print(f"Error: {e}")