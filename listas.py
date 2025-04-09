numeros = [1, 2, 3]
letras = ["a", "b", "c"]

agregar_numero = int(input("digita un nuevo numero: "))
numeros.append(agregar_numero)

for i in numeros:
    print(i)

# buscar_numero = int(input("digite un numero a buscar: "))

# if buscar_numero in numeros:
#     index = numeros.index(buscar_numero)
#     print("numero encontrado")
#     print("index", index)

# else:
#     print("numero no encontrado")

numero_eliminar = int(input("digite un numero a eliminar: "))

if numero_eliminar in numeros:
    opc = int(
        input(
            "si esta seguro de eliminar el numero digite (1), caso contrario cualquier otro caracter: "
        )
    )
    if opc == 1:
        numeros.remove(numero_eliminar)
        print("numero eliminado")
    else:
        print("numero no eliminado")
else:
    print("el numero no existe")

print(numeros)
