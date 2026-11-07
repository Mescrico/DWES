# Añade validación con raise a aplicar_descuento: además del porcentaje, el precio debe ser positivo. 
# Escribe después las llamadas que provoquen cada error y captúralas por separado.

def aplicar_descuento(precio, porcentaje):
    if precio < 0:
        raise ValueError("El precio debe ser positivo")
    if not 0 <= porcentaje <= 100:    
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return precio * (1 - porcentaje / 100)

# Precio Negativo
aplicar_descuento(-200, 30)
# Porcentaje Erroneo
aplicar_descuento(200, 130)