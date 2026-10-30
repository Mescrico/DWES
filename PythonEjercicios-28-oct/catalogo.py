def producto_mas_caro(catalogo):
    
    mas_caro = catalogo[0]
    
    for producto in catalogo:
        
        if producto["precio"] > mas_caro["precio"]:
            
            mas_caro = producto
    
    return mas_caro


def saludar():
    
    print("Módulo de catálogo cargado")

def productos_agotados(catalogo):
    agotados = []
    for producto in catalogo:
        if producto["stock"] <= 0:
            agotados.append(producto)    
    return agotados
if __name__ == "__main__":
    
# esto solo se ejecuta si lanzas: python3 catalogo.py
    
# no se ejecuta cuando tienda.py hace: from catalogo import ...
    
    saludar()
