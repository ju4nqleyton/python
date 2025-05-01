departamentos = {}


def ingresar_departamento(nombre, capital, habitantes, diccionario):
    diccionario[nombre] = (capital, habitantes)
    # print(nombre, capital, habitantes)
    # print(diccionario)
    print("departamento ingresado correctamente")


def buscar(departamento, dicionario):
    if (departamento) in dicionario:
        print(f"{departamento} si se encuentra guardado")
        print(dicionario[departamento])
    else:
        print(f"{departamento} no se encuentra guardado")
    # print(departamento, departamentos)


def modificar_capital(departamento, capital_nueva, diccionario):
    if (departamento) in diccionario:
        # copia_diccionario = diccionario.copy()
        habitantes = diccionario[departamento][1]
        # print({"habitantes", habitantes})
        # print("copia", copia_diccionario)
        # print(diccionario[modificar])
        diccionario[departamento] = capital_nueva, habitantes
        print("capital modificada correctamente")
        # print(diccionario)
    else:
        print(f"departamento: {departamento} no existe")


def eliminar_departamento(departamento, diccionario):
    if (departamento) in diccionario:
        del diccionario[departamento]
        print("eliminado con exito")
    else:
        print(f"{departamento} no existe")


def mostrar_departamentos(diccionario):
    print(f"departamentos guardados:\n{diccionario}")


while True:
    accion = input(
        f"(1) ingresar\n(2) buscar\n(3) modificar capital\n(4) eliminar\n(5) ver\naccion: "
    )
    if accion not in ["1", "2", "3", "4", "5"]:
        print("accion invalida")
        accion = input(
            f"(1) ingresar\n(2) buscar\n(3) modificar capital\n(4) eliminar\n(5) ver\naccion: "
        )
    elif accion == "1":
        nombre = input("nombre departamento: ")
        capital = input("capital: ")
        habitantes = int(input("habitantes: "))
        ingresar_departamento(nombre, capital, habitantes, departamentos)
    elif accion == "2":
        departamento = input("buscar: ")
        buscar(departamento, departamentos)
    elif accion == "3":
        departamento_modificar = input("departamento: ")
        capital_nueva = input("nueva capital: ")
        modificar_capital(departamento_modificar, capital_nueva, departamentos)
    elif accion == "4":
        departamento_eliminar = input("departamento a eliminar: ")
        eliminar_departamento(departamento_eliminar, departamentos)
    elif accion == "5":
        mostrar_departamentos(departamentos)

# ingresar_departamentos()
# buscar("tolima", departamentos)
# modificar(departamentos[tolima], departamentos[cali], departamentos)
# print(departamentos)
