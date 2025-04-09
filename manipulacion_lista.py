numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

opc = 1
# accion = int(input("(1) agrega, (2) elimina, (3) modifica, (4) muestra: "))

while opc == 1:
    accion = int(
        input(
            "(1) agrega, (2) elimina, (3) modifica, (4) muestra, (5) calcular el promedio: "
        )
    )

    if accion == 1:
        numero_agregar = int(input("numero a agregar: "))
        numeros.append(numero_agregar)
        print(f"{numero_agregar} numero agregado")
    elif accion == 2:
        numero_eliminar = int(input("numero a eliminar: "))
        if numero_eliminar in numeros:
            numeros.remove(numero_eliminar)
            print(f"{numero_eliminar} numero eliminado")
        else:
            print(f"el numero {numero_eliminar} no existe en la lista")
    elif accion == 3:
        numero_modificar = int(input("numero a modificar: "))
        if numero_modificar in numeros:
            posicion_numero = numeros.index(numero_modificar)
            numeros.remove(numero_modificar)
            nuevo_numero = int(input("digite el nuevo valor: "))
            numeros.insert(posicion_numero, nuevo_numero)
            print(f"numero {nuevo_numero} modificado con exito")
        else:
            print(f"el numero {numero_modificar} no existe en la lista")
    elif accion == 4:
        print(numeros)
    elif accion == 5:
        acumulador = 0
        for i in range(len(numeros)):
            acumulador += numeros[i]
        print("primer acumulador", acumulador)
        promedio = acumulador // len(numeros)
        print(f"el promedio de la lista es {promedio}")
        acumulador = 0
        print("segundo acumulador", acumulador)
        print("tamaño de lista", len(numeros))

    else:
        print("digite una opcion valida")
    opc = int(input("(1) para repetir proceso, cualquier otro caracter para salir: "))
