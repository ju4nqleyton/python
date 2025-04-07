# valor = int(input("El valor de su compra sin descuento es: "))
# print("valor", valor)
# descuento = int(valor * 0.15)
# print("descuento", descuento)
# valorTotal = valor - descuento
# print("total a pagar: ", valorTotal)

valorCompra = int(input("valor compra: "))
# print("valor compra", valorCompra)
descuentoPorcentual = int(input("digite el porcentaje del descuento: "))
# print(descuentoPorcentual)
descuento = descuentoPorcentual / 100
valorTotal = int(valorCompra * descuento)
print(valorTotal)
