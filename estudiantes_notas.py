# entrada -> estudiantes/notas
# proceso ->
# salida -> #estudiantes, promedio_notas, mejor_estudiante, peor_estudiante

# el usuaria decide cuantos estudiantes ingresar
# captura nombre y respectiva nota
# fin para terminar

# mostrar cuantos estudiantes se registraron
# promedio de todas las notas
# estudiante mas alta nota
# estudiante mas baja nota

estudiantes = []
notas = []

while True:
    estudiante = input("nombre estudiante: ")
    if estudiante == "fin":
        break

    nota = float(input("digite la calificacion: "))
    while nota < 0 or nota > 5:
        nota = float(input("digite una nota correcta: "))

    print("estudiante: ", estudiante)
    print("nota: ", nota)

    estudiantes.append(estudiante)
    notas.append(nota)

    print("estudiantes: ", estudiantes)
    print("notas: ", notas)

numero_estudiantes = len(estudiantes)
promedio = sum(notas) / numero_estudiantes

print("numero_estudiantes", numero_estudiantes)
print("promedio", promedio)

if len(notas) > 0:
    nota_maxima = max(notas)
    posicion_maxima = notas.index(nota_maxima)
    mejor_estudiante = estudiantes[posicion_maxima]

    nota_minima = min(notas)
    posicion_minima = notas.index(nota_minima)
    peor_estudiante = estudiantes[posicion_minima]

    print("posicion_maxima", posicion_maxima)
    print("mejor_estudiante", mejor_estudiante)
    print("posicion_minima", posicion_minima)
    print("peor_estudiante", peor_estudiante)
