# Reto: reescribe la clase Articulo del apartado @dataclass a mano (constructor, __repr__ y __eq__) 
# y compara línea a línea lo que el decorador te ahorró. Comprueba que != sigue funcionando aunque no lo hayas escrito. 
# Añade después un método propio valor_stock() y verifica que una dataclass admite métodos como cualquier otra clase.

from dataclasses import dataclass


@dataclass
class Articulo:
    nombre: str    
    precio: float    
    stock: int = 0
    
    # def __init__(self, nombre: str, precio: float, stock: int = 0):
    #    self.nombre = nombre
    #    self.precio = precio
    #    self.stock = stock
    
    # def __str__(self):
    #    return f"{self.nombre} - {self.precio} €, {self.stock} uds"
    
    # def __repr__(self):
    #    return f"Articulo(nombre: {self.nombre}, precio: {self.precio}, stock: {self.stock})"

    # def __eq__(self, otro):
    #    if not isinstance(otro, Articulo):
    #        return NotImplemented
    #    return (self.nombre == otro.nombre and 
    #            self.precio == otro.precio and 
    #            self.stock == otro.stock)
    
    def valor_stock(self):
        return self.precio*self.stock
    
    

art1 = Articulo("Teclado", 45.0, 10)
art2 = Articulo("Teclado", 45.0, 10)
art3 = Articulo("Ratón", 20.0, 5)

# Compruebo que != sigue funcionando (tiene que dar true)
print(f"1 != 2: {art1 != art2}")