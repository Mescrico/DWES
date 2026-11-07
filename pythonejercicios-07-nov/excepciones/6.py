# Crea dos excepciones propias para validar altas de producto: NombreVacioError y PrecioInvalidoError. 
# Escribe crear_producto(nombre, precio) que devuelva el diccionario {"nombre": nombre, "precio": precio} 
# solo si el nombre no está vacío y el precio es positivo, lanzando cada excepción con un mensaje claro; 
# captúralas por separado en el programa principal. 
# Después crea una base común ErrorProducto de la que hereden ambas y comprueba que un único except ErrorProducto las captura a las dos

class ErrorProducto(Exception):
    pass

class NombreVacioError(ErrorProducto):
    pass

class PrecioInvalidoError(ErrorProducto):
    pass

def crear_producto(nombre, precio):
    diccionario = {}

    if nombre is not None and precio >= 0:
        diccionario["nombre"] = nombre
        diccionario["precio"] = precio
    elif not nombre or nombre is None or not nombre.strip():
        raise NombreVacioError("El nombre no puede estar vacío")
    elif precio < 0:
        raise PrecioInvalidoError("El precio no puede ser negativo")
    return diccionario

try:
    producto = crear_producto(None, 450)
    print(f"Producto creado {producto}")
except ErrorProducto as e:
    print(f"Se ha producido un error: {e}")

