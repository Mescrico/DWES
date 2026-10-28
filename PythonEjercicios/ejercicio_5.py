# Pide al usuario que ingrese una frase larga. Luego, pide que ingrese dos números para seleccionar una subcadena desde el índice de inicio hasta el índice de fin, e imprime la subcadena seleccionada.
fraseLarga = str(input("Escribe una frase larga: "))
primer = int(input("Escribe el indice de inicio: "))
segundo = int(input("Escribe el indice de fin: "))

fraseCortada = fraseLarga[primer:segundo]
print(fraseCortada)