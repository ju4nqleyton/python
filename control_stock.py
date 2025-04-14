productos = []

while True:
    nombre = input("nombre producto: ")
    if nombre == "fin":
        break

    precio = int(input("precio producto: "))
    while precio < 0 or precio > 10000:
        precio = int(input("ingrese precio correcto: "))

    cantidad = int(input("cantidad producto: "))
    while cantidad < 0 or cantidad > 1000:
        cantidad = int(input("ingrese cantidad correcta: "))

    productos.append((nombre, precio, cantidad))
    # print(productos)

if productos:
    producto_mas_cantidad = productos[0]
    producto_mas_costoso = productos[0]
    precios_totales = []

    for nombre, precio, cantidad in productos:
        print(f"producto: {nombre} ${precio} - stock: {cantidad}")

        if cantidad > producto_mas_cantidad[2]:
            producto_mas_cantidad = (nombre, precio, cantidad)

        if precio > producto_mas_costoso[1]:
            producto_mas_costoso = (nombre, precio, cantidad)

        precios_totales.append(cantidad * precio)

    precio_total = sum(precios_totales)

    print(
        f"producto mas cantidad: {producto_mas_cantidad[0]} - stock: {producto_mas_cantidad[2]}"
    )
    print(
        f"producto mas costosos: {producto_mas_costoso[0]} ${producto_mas_costoso[1]}"
    )
    print(f"precio total inventario: ${precio_total}")
