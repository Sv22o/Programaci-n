import json

def nuevo_alumno(nombre, apellido, cedula, nota1, nota2, nota3): #se utiliza para crear al nuevo alumno
    datos_alumno = {'nombre': nombre, 'apellido': apellido, 'cedula': cedula, 'nota1': nota1, 'nota2': nota2, 'nota3': nota3}
    with open('alumnos.json', 'r') as files:
        alumnos_1 = []
        alumnos_1.append(nuevo_alumno)
        with open('alumnos.json', 'w') as files:
            json.dump(alumnos_1, files, indent = 4)

def mostrar_alumnos(datos): #permite mostrar la lista de alumnos
    return datos['data']
    
while True:
    opcion = int(input('que desea hacer? escriba 1 para crear un nuevo alumno, 2 para mostrar la lista de alumnos y 3 para salir: '))
    if opcion == 1:
        nombre = input('nombre del alumno: ')
        apellido = input('apellido del alumno: ')
        cedula = input('cedula del alumno: ')
        nota1 = input('nota1 del alumno: ')
        nota2 = input('nota2 del alumno: ')
        nota3 = input('nota3 del alumno: ')
        nuevo_alumno(nombre, apellido, cedula, nota1, nota2, nota3)
        print(f'el alumno {nombre} {apellido} se creó correctamente')
    elif opcion == 2:
        mostrar = mostrar_alumnos(datos):
        for dato in alumnos:
            print(dato)
    elif opcion == 3:
        break



