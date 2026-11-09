vinos_jerez = [
    "Sherry Classic",
    "Vino Blanco",
    "Fino SHERRY",
    "Moscatel",
    "ShErry Cream"
]

def estaSherry(listaVinos):
    """Funcion para calcular si esta dentro de cada posicion de la lista Sherry"""
    diccionario = {}
    listaVinosSherry = []

    for nombre in listaVinos:
        nombreFormateado = nombre.strip().title()
        if "Sherry" in nombreFormateado:
            diccionario[nombre] = True
        else:
            diccionario[nombre] = False
    listaVinosSherry = filter(lambda v: "Sherry" in v.strip().title(), listaVinos)
    return diccionario, listaVinosSherry

dic, lista = estaSherry(vinos_jerez)

print(f"Diccionario de vinos: {dic}")

print(f"Lista de vinos con 'Sherry': {list(lista)}")