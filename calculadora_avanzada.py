def calcular_voltaje(i, r):
    voltaje = i * r
    return voltaje


def calcular_resistencia(v, i):
    resistencia = v / i
    return resistencia


def calcular_intensidad(v, r):
    intensidad = v / r
    return intensidad


opc = 1

while opc == 1:
    accion = int(
        input(
            "(1) calcular voltaje, (2) calcular resistencia, (3) calcular intensidad: "
        )
    )
    if accion not in [1, 2, 3]:
        print("seleccione una opcion valida")

    if accion == 1:
        intensidad = int(input("digite la intensidad: "))
        resistencia = int(input("digite la resistencia: "))
        calcular_voltaje(intensidad, resistencia)
    elif accion == 2:
        voltaje = int(input("digite el voltaje: "))
        intensidad = int(input("digite la intensidad: "))
        calcular_resistencia(voltaje, intensidad)
    elif accion == 3:
        voltaje = int(input("digite el voltaje: "))
        resistencia = int(input("digite la resistencia: "))

    opc = int(
        input(
            "si desea otra operacion de nuevo digite (1), para salir cualquier otro caracter: "
        )
    )
