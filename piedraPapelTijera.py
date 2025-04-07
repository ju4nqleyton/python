import random

play = 1

while play == 1:
    aleatorio = random.randint(1, 3)
    # print("numero aleatorio", aleatorio)
    accion = int(input("(1) piedra, (2) papel, (3) tijeras: "))

    if accion != 1 or accion != 2 or accion != 3:
        print("seleccione una opcion valida")
    elif accion == aleatorio:
        print("empate, ambos sacaron lo mismo")
    elif accion == 1 and aleatorio == 2:
        print("la maquina saco papel, y te gano")
    elif accion == 1 and aleatorio == 3:
        print("felicidades la maquina saco tijeras, le ganaste")
    elif accion == 2 and aleatorio == 3:
        print("la maquina saco tijeras, y te gano")
    elif aleatorio == 1 and accion == 2:
        print("felicidades la maquina saco papel, le ganaste")
    elif aleatorio == 1 and accion == 3:
        print("la maquina saco tijeras, y te gano")

    play = int(
        input("si desea jugar de nuevo digite (1), para salir cualquier otra letra: ")
    )
