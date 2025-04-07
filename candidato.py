candidato = input("seleccione el candidato por el cual va a votar: ")
# print("candidato", candidato)

if candidato == "A" or candidato == "a":
    print("usted ha votado por el partido rojo")
elif candidato == "B" or candidato == "b":
    print("usted ha votado por el partido verde")
elif candidato == "C" or candidato == "c":
    print("usted ha votado por el partido azul")
else:
    print("opcion erronea")
