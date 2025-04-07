contador = 0
acumulador = 0

while contador != 4:
    nota = int(input("digite una nota: "))
    # print("nota", nota)
    if nota > 5 or nota < 0:
        print("por favor digite una nota valida")
    else:
        contador += 1
        acumulador += nota

promedio = acumulador / contador
print("el promedio de las notas fue: ", promedio)
