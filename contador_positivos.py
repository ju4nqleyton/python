# entrada -> numeros
# proceso -> filtrar solo numeros positivos
# salida -> candidad de numeros positivos

# capturar los numeros (0 termina)
# recorerrer los numeros
# filtro positivos y negativos (lista)
# muestro el output

numeros = []
positivos = []

while True:
    numero = int(input("digite un numero: "))
    if numero == 0:
        break
    # print("numero", numero)
    numeros.append(numero)
    # print("numeros", numeros)

for i in numeros:
    # print("i", i)
    if i > 0:
        positivos.append(i)

# print("contador positivos", contador_positivos)

if len(positivos) > 0:
    promedio = sum(positivos) / len(positivos)

print(
    f"en total fueron {len(positivos)} numeros positivos y el promedio fue {promedio}"
)
