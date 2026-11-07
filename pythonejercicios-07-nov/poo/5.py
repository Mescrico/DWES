# Crea la clase Formacion (nombre del curso y precio) con su precio_con_iva(). 
# Mete productos, productos rebajados y formaciones en la misma lista y calcula el total con total_con_iva. 
# Añade después una clase ServicioPremium olvidando a propósito el método precio_con_iva, 
# inclúyela en la lista y observa el AttributeError: ¿en qué línea salta y por qué no lo vio nadie antes?

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

class Formacion:
    def __init__(self, nombreCurso, precio):
        self.nombreCurso = nombreCurso
        self.precio = precio
    
    def precio_con_iva(self):
        return self.precio*1.21
    
    def __str__(self):
        return f"{self.nombreCurso} - {self.precio} €"

class ProductoRebajado(Producto):
    def __init__(self, nombre, precio, stock, descuento):
        super().__init__(nombre, precio, stock)
        self.descuento = descuento
    
    def precio_con_iva(self):
        precio_con_descuento = self.precio * (1 - self.descuento_porcentaje / 100)
        return precio_con_descuento * 1.21
    
    def __str__(self):
        return f"{self.nombre} - {self.precio} € , {self.stock} uds , {self.descuento} %"

p_normal = Producto("Teclado", 30.0, 10)
p_rebajado = ProductoRebajado("Cascos Gaming", 50.0, 5, 20)
curso = Formacion("Curso avanzado de Python", 120.0)

lista = [p_normal, p_rebajado, curso]

total_con_iva = 0

for producto in lista:
    total_con_iva = total_con_iva + producto.precio_con_iva()
    print(producto)
    print(f"Precio con iva {producto.precio_con_iva():.2f}")

print(f"Total con iva: {total_con_iva:.2f}") 