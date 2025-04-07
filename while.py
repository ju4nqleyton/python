opc = 1

while opc == 1:
    edad = int(input("digite la edad: "))
    if edad >= 18:
        print("es mayor de edad")
    else:
        print("es menor de edad")
    opc = int(input("para continuar presione 1, de lo contrario session finalizada: "))
print("seccion finalizada")
