# entrada -> palabra o frase * string
# proceso -> encontrar numero de vocales * recorrer el string
# salida -> numero de vocales

# tendria que pedir una palabra o una frase al usuario
# string, tengo que encontrar la forma de poder recorrer la palabra o string y contar vocales

# pido la palabra al usuario

palabra = str(input("digite la palabra o frase: "))
# print(len(palabra), "palabra")


contador = 0

for caracteres in palabra:
    # print(caracteres)
    caracter = caracteres

    if (
        caracter == "a"
        or caracter == "A"
        or caracter == "e"
        or caracter == "E"
        or caracter == "i"
        or caracter == "I"
        or caracter == "o"
        or caracter == "O"
        or caracter == "u"
        or caracter == "U"
    ):
        # print(caracter)
        contador += 1

# print("contador", contador)
print(f"la palabra/frase tiene {contador} vocal(es)")

### -----------------------------------------------------

# frase = input("Digite la palabra o frase: ")
# contador = 0

# for caracter in frase:
#    if caracter.lower() in ["a", "e", "i", "o", "u"]:
#       contador += 1
#
# print(f"La palabra/frase tiene {contador} vocal(es)")
