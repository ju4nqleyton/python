opc = 1
contador = 0
acumulador = 0

while opc == 1:
    edad = int(input("digite una edad: "))
    # print("edad", edad)
    contador += 1
    # print("contador", contador)
    acumulador += edad
    # print("acumulador", acumulador)
    opc = int(input("para continuar presione 1, caso contrario terminara: "))

promedio = int(acumulador / contador)
print("el promedio de las edades fue: ", promedio)
