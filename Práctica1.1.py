calificacion = int(input('Ingrese la calificación: '))
if calificacion < 0 or calificacion > 100:
    print('Calificación inválida')
elif calificacion == 100:
    print('Calificación perfecta')
elif calificacion >= 90:
    print('Excelente')
elif calificacion >= 70:
    print('Bueno')
elif calificacion >= 50:
    print('Suficiente')
elif calificacion < 50:
    print('Insuficiente')
