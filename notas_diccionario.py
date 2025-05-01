notas = {}


def ingresar_estudiante(estudiante, diccionario):
    diccionario[estudiante]
    print("estudiante ingresado correctamente")


def ingresar_notas(estudiante, notas, diccionario):
    diccionario[estudiante] = [notas]


def buscar_estudiante(estudiante, diccionario):
    if (estudiante) in diccionario:
        print(f"{estudiante} encontrado con exito:\n{diccionario[estudiante]}")
    else:
        print(f"{estudiante} no ha sido encontrado")


def modificar_notas():
    print("modificar notas")


def eliminar_estudiantes(estudiante, diccionario):
    if (estudiante) in diccionario:
        del diccionario[estudiante]
        print("estudiante eliminado correctamente")
    else:
        print("estudiante no existe")


def mostrar_estudiantes(diccionario):
    print(f"estudiantes:\n{diccionario}")


while True:
    accion = input(
        f"(1) ingresar estudiante\n(2) buscar estudiante\n(3) modificar notas\n(4) eliminar estudiante\n(5) ver estudiantes\naccion: "
    )
    if accion not in ["1", "2", "3", "4", "5", "6"]:
        print("accion invalida")
        accion = input(
            f"(1) ingresar estudiante\n(2) buscar estudiante\n(3) modificar notas\n(4) eliminar estudiante\n(5) ver estudiantes\naccion: "
        )
