from catalogo import producto_mas_caro, productos_agotados

catalogo = [
    {"nombre": "Cuaderno", "precio": 2.5, "stock": 12},
    {"nombre": "Mochila", "precio": 18.9, "stock": 3},
    {"nombre": "Lapiz", "precio": 14.3, "stock": 0},
    {"nombre": "Goma", "precio": 3.5, "stock": 0},
    {"nombre": "Sacapuntas", "precio": 16.7, "stock": 0}
]

agotados = productos_agotados(catalogo)
caro = producto_mas_caro(catalogo)
print(f"El más caro es {caro['nombre']}: {caro['precio']:.2f} €")

agotadosOrdenados = sorted(agotados, key=lambda p: p["precio"])
print(agotadosOrdenados)
