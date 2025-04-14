# entrada -> productos
# proceso -> recorrerlos
# salida -> cuales, cuantos, promedio, precio_alto

productos = []

while True:
    nombre = input("nombre producto: ")
    if nombre == "fin":
        break

    precio = int(input("precio producto: "))
    while precio < 0:
        precio = int(input("digite precio correcto: "))

    productos.append((nombre, precio))
    # print(productos)

if productos:
    suma = 0
    producto_mas_costoso = productos[0]
    for nombre, precio in productos:
        suma += precio
        print(f"producto: {nombre} - ${precio}")
        # print("precio", precio)
        # print("suma", suma)

        if precio > producto_mas_costoso[1]:
            producto_mas_costoso = (nombre, precio)

    promedio = suma / len(productos)

    # print("promedio", promedio)
    # print("producto_mas_costoso", producto_mas_costoso)
    print(f"\n# productos productos: {len(productos)}")
    print(f"promedio precios: {promedio:.2f}")
    print(f"producto costoso: {producto_mas_costoso[0]} (${producto_mas_costoso[1]})")

# print(len(productos))
# print(suma)
