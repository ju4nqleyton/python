import getpass

admin = "4444"
eventos = {}


def crear_evento(eventos):
    nombre = input("nombre del evento --> ")
    descripcion = input("descripcion del evento --> ")
    lugar = input("lugar del evento --> ")
    hora = input("hora del evento --> ")
    eventos[nombre] = {"descripcion": descripcion, "lugar": lugar, "hora": hora}
    print("evento creado con exito")


def listar_eventos(eventos):
    if len(eventos) == 0:
        print(f"no hay eventos creados")
    else:
        print(f"hay un total de {len(eventos)} eventos para hoy:")
        for evento, detalles in eventos.items():
            print(f"\nevento: {evento}")
            print(f"descripción: {detalles['descripcion']}")
            print(f"lugar: {detalles['lugar']}")
            print(f"hora: {detalles['hora']}")


def consultar_evento(eventos):
    if len(eventos) == 0:
        print("no hay eventos creados")
    else:
        evento = input("escriba el evento a consultar --> ")
        if evento in eventos:
            detalles = eventos[evento]
            print(f"\nevento: {evento}")
            print(f"descripción: {detalles['descripcion']}")
            print(f"lugar: {detalles['lugar']}")
            print(f"hora: {detalles['hora']}")
        else:
            print(f"el evento no existe")


def modificar_evento(eventos):
    if len(eventos) == 0:
        print("no hay eventos creados")
        return

    evento = input("escriba el nombre del evento a modificar --> ")
    if evento not in eventos:
        print(f"el evento no existe")
        return

    while True:
        accion = input(
            "(1) modificar nombre\n(2) modificar descripción\n(3) modificar lugar\n(4) modificar hora\n(5) volver\nescoja una opción --> "
        )

        if accion == "1":
            nuevo_nombre = input("ingrese nuevo nombre del evento --> ")
            eventos[nuevo_nombre] = eventos.pop(evento)
            print("nombre del evento modificado con exito")
            evento = nuevo_nombre
        elif accion == "2":
            nueva_descripcion = input("ingrese nueva descripcion --> ")
            eventos[evento]["descripcion"] = nueva_descripcion
            print("descripcion modificada con exito")
        elif accion == "3":
            nuevo_lugar = input("ingrese nuevo lugar --> ")
            eventos[evento]["lugar"] = nuevo_lugar
            print("lugar modificado con exito")
        elif accion == "4":
            nueva_hora = input("ingrese nueva hora --> ")
            eventos[evento]["hora"] = nueva_hora
            print("hora modificada con exito")
        elif accion == "5":
            break
        else:
            print("opcion incorrecta")


def eliminar_evento(eventos):
    if len(eventos) == 0:
        print("no hay eventos creados")
    else:
        evento = input("escriba el evento a eliminar --> ")
        if (evento) in eventos:
            del eventos[evento]
            print("evento eliminado con exito")
        else:
            print("el evento no existe")


while True:
    clave = ""
    accion = input(
        f"(1) administrador\n(2) invitado\n(3) salir\nescoja una opcion --> "
    )

    if accion not in ["1", "2", "3"]:
        print("accion incorrecta")
        accion = input(
            f"(1) administrador\n(2) invitado\n(3) salir\nescoja una opcion --> "
        )

    if accion == "3":
        print("session finalizada")
        break

    while accion == "1":
        if clave == "":
            clave = getpass.getpass("ingrese clave --> ")

        if clave == admin:
            print("modo administrador")
            opc = input(
                "(1) crear evento\n(2) listar eventos\n(3) consultar eventos\n(4) modificar evento\n(5) eliminar evento\n(6) volver\nescoja una opcion --> "
            )
            if opc not in ["1", "2", "3", "4", "5", "6"]:
                print("opcion incorrecta")
                opc = input(
                    "(1) crear evento\n(2) listar eventos\n(3) consultar eventos\n(4) modificar evento\n(5) eliminar evento\n(6) volver\nescoja una opcion --> "
                )
            elif opc == "1":
                crear_evento(eventos)
            elif opc == "2":
                listar_eventos(eventos)
            elif opc == "3":
                consultar_evento(eventos)
            elif opc == "4":
                modificar_evento(eventos)
            elif opc == "5":
                eliminar_evento(eventos)
            else:
                break
        else:
            print("clave incorrecta")
            break

    while accion == "2":
        print("modo invitado")
        opc = input("(1) ver eventos\n(2) volver\nescoja una opcion --> ")

        if opc not in ["1", "2"]:
            print("opcion incorrecta")
            opc = input("(1) ver eventos\n(2) volver\nescoja una opcion --> ")
        elif opc == "1":
            listar_eventos(eventos)
        else:
            break
