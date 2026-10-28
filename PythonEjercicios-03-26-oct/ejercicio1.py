nota = int(input("Escribe una nota entera: "))

if nota < 5:
    print("Insuficiente")
elif nota <= 6:
    print("Suficiente")
elif nota <= 7:
    print("Bien")
elif nota <= 9:
    print("Notable")
elif nota <= 10:
    print("Sobresaliente")

ternaria = "Insuficiente" if nota < 5 else "Suficiente" if nota <= 6 else "Bien" if nota <= 7 else "Notable" if nota <= 9 else "Sobresaliente"

print(f"Y en ternario: {ternaria}")