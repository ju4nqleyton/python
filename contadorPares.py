contador = 0
acumulador = 0

for i in range(0, 21):
    if i % 2 == 0:
        contador = contador + 1
        acumulador += i
    print(i, "es un numero par")

print("se encontraron: ", contador, "numeros pares")
print("la suma de todos los numeros pares es: ", acumulador)
