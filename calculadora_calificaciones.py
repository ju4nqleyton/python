primera_calificacion = int(input("primera calificacion: "))
segunda_calificacion = int(input("segunda calificacion: "))
tercera_calificacion = int(input("tercera calificacion: "))
examen_final = int(input("examen final: "))
trabajo_final = int(input("trabajo final: "))

porcentaje_parciales = (
    (primera_calificacion + segunda_calificacion + tercera_calificacion) / 3
) * 0.55
porcentaje_examen_final = examen_final * 0.30
porcentaje_trabajo_final = trabajo_final * 0.15
notal_final = porcentaje_parciales + porcentaje_examen_final + porcentaje_trabajo_final
print("su nota final es: ", notal_final)
