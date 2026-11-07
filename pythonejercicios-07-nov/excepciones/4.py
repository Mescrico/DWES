# Con el catálogo de la página 4, escribe buscar_producto(catalogo, nombre) que devuelva el diccionario o lance ValueError("Producto no encontrado"). 
# Captura el error en el programa principal y muéstralo amablemente.

catalogo = [    
    {"nombre": "Cuaderno", "precio": 2.5, "stock": 12},       
    {"nombre": "Lápiz", "precio": 0.8, "stock": 0},  
    {"nombre": "Mochila", "precio": 18.9, "stock": 3},
]

def buscar_producto(catalogo, nombre):
    for producto in catalogo:
        if nombre in producto["nombre"]:
            return print(producto)
    raise ValueError("Producto no encontrado")

# Lo encuentra
buscar_producto(catalogo, "Cuaderno")
# No lo encuentra
buscar_producto(catalogo, "Estuche")