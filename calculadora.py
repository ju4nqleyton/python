def suma(a, b):
    resultado = a + b
    print(resultado)
    return resultado


def resta(a, b):
    resultado = a - b
    print(resultado)
    return resultado


def multiplicacion(a, b):
    resultado = a * b
    print(resultado)
    return resultado


def dividir(a, b):
    resultado = a / b
    print(resultado)
    return resultado


# opc = 1

# while opc == 1:
#     accion = int(input("(1) sumar, (2) restar, (3) multiplicar, (4) dividir: "))
#     if accion not in [1, 2, 3, 4]:
#         print("seleccione una opcion valida")

#     primer_numero = int(input("digite el primer numero: "))
#     segundo_numero = int(input("digite el segundo numero: "))

#     if accion == 1:
#         suma(primer_numero, segundo_numero)
#     elif accion == 2:
#         resta(primer_numero, segundo_numero)
#     elif accion == 3:
#         multiplicacion(primer_numero, segundo_numero)
#     elif accion == 4:
#         dividir(primer_numero, segundo_numero)

#     opc = int(
#         input(
#             "si desea otra operacion de nuevo digite (1), para salir cualquier otro caracter: "
#         )
#     )
