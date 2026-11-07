# Amplía el catálogo con una clase ProductoDigital que herede de Producto y su __init__ llame a super() para añadir tamano_mb.
# Razona qué versión de precio_con_iva se ejecuta para cada tipo de la lista y demuéstralo con isinstance.

class Formacion:
    def __init__(self, nombreCurso, precio):
        self.nombreCurso = nombreCurso
        self.precio = precio
    
    def precio_con_iva(self):
        return self.precio*1.21
    
    def __str__(self):
        return f"{self.nombreCurso} - {self.precio} €"

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
    
    def precio_con_iva(self):
        return self.precio*1.21

class ProductoDigital(Producto):
    def __init__(self, nombre, precio, stock, tamano_mb):
        super().__init__(nombre, precio, stock)
        self.tamano_mb = tamano_mb

p_normal = Producto("Teclado", 30.0, 10)
p_digital = ProductoDigital("E-Book Python Avanzado", 25.0, 100, 15.5)
curso = Formacion("Curso de Arquitectura", 120.0)

lista = [p_normal, p_digital, curso]

for producto in lista:
    if isinstance(producto, Producto):
        print(f"{producto} es de Producto")
    if isinstance(producto, ProductoDigital):
        print(f"{producto} es de ProductoDigital")
    if isinstance(producto, Formacion):
        print(f"{producto} es de Formacion")