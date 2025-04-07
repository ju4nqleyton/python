edad = int(input("digite su edad: "))
print("edad", edad)

if edad > 100 or edad < 0:
    print("edad invalida")
elif edad > 65:
    print("es un adulto mayor")
elif edad > 17:
    print("es un adulto")
elif edad > 13:
    print("es un adolescente")
elif edad > 3:
    print("es menor de edad")
else:
    print("es un bebe")
