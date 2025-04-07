primera_nota = float(input("digite la primera nota: "))
segunda_nota = float(input("digite la segunda nota: "))
tercera_nota = float(input("digite la tercera nota: "))

if primera_nota > 5 or primera_nota < 0:
    print("primera nota invalida")
    exit()
elif segunda_nota > 5 or segunda_nota < 0:
    print("segunda nota invalida")
    exit()
elif tercera_nota > 5 or tercera_nota < 0:
    print("tercera nota invalida")
    exit()

promedio_calificaciones = (primera_nota + segunda_nota + tercera_nota) / 3

if promedio_calificaciones >= 4.5:
    print("felicidades aprobo")
    print("rendimiento excelente")
elif promedio_calificaciones >= 3 and promedio_calificaciones <= 4.4:
    print("felicidades aprobo")
    print("rendimiento bueno")
elif promedio_calificaciones >= 2 and promedio_calificaciones <= 2.9:
    print("lo sentimos, reprobo")
    print("rendimiento malo")
else:
    print("lo sentimos, no aprobo")
    print("rendimiento minimo")
