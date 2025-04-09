# entrada -> frase
# proceso -> encontrar cuantas palabras tiene la frase
# salida -> numero de palabras

# capturar la frase
# separar la frase con .split
# guardar cada bloque en una lista
# mostrar la longitud de la lista

frase = input("digite una frase: ")
print("frase", frase)

palabras = frase.split()
print("palabras", palabras)

print(f"la frase tiene un total de {len(palabras)} palabras")
