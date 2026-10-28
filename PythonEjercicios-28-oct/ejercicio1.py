# Reescribe como función, con docstring y anotaciones de tipos, la solución del ejercicio 4 de la página anterior (producto más caro del catálogo). Comprueba que help() muestra vuestro docstring.
def producto_mas_caro(catalogo: list) -> float:
    """Calcula el producto mas caro de una lista"""
    precios = [];
    for producto in catalogo:
        precios.append(producto["precio"])
    for producto in catalogo:
        if producto["precio"] == max(precios):
            productoCaro = producto
            break
    return productoCaro

help(producto_mas_caro)