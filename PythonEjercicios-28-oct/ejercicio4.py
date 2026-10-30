import random
contador = {}

cont =  0

while cont < 100:
    numero = random.randint(1,6)
    if numero not in contador:
        contador[numero] = 1
    else:
        contador[numero] += 1
    cont += 1
print(contador[6])