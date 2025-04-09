# entrada -> tres numeros enteros
# proceso -> determinar cual es el mayor
# salida -> el numero mayor

# capturo los tres numeros enteros
# por medio de condicionales identifico cual es el mayor
# muestro con un print el mayor

primer_numero = int(input("digite el primer numero: "))
segundo_numero = int(input("digite el segundo numero: "))
tercero_numero = int(input("digite el tercero numero: "))

# print("primer numero", primer_numero)
# print("segundo numero", segundo_numero)
# print("tercero numero", tercero_numero)

numeros = [primer_numero, segundo_numero, tercero_numero]
# print("numeros", numeros)

numeros.sort(reverse=True)
print(numeros[0])
