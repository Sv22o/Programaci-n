#ejercicio 3:
abc = 'abcdefghijklmnopqrstuvwxyz'
lista_abc = list(abc)
lista_abc1 = []
lista_numeros = []
for i in range(1,108):
    acumulador = 0
    for j in range(1,i+1):
        if i % j == 0:
            acumulador += 1
        if acumulador == 2:
            lista_numeros.append(i)

while True:
    opcion1 = ("1.codificar")
    opcion2 = ("2.decodificar")
    opcion3 = ("3.contar frecuencia")
    opcion4 = ("4.salir")
    opciones = dict([("opcion1", opcion1), ("opcion2", opcion2), ("opcion3", opcion3), ("opcion4", opcion4)])
    for opcionesusuarios in opciones:
        print(opciones[opcionesusuarios])

    codificar = ''
    decodificar = ''
    opc_usuario = input('ingrese la opcion que desee(coloque el numero): ')
    letras = 0
    if opc_usuario == '4':
        print('Finalizó el programa')
        break
    elif opc_usuario == '1':
        palabra = input('Ingrese el mensaje que desea codificar: ')
        for letra in palabra:
            for letrilla in range(len(abc)):
                if letra == abc[letrilla]:
                    letra = str(lista_numeros[abc.index(letra)])
                    codificar += ('-') + letra
            if codificar and codificar[0] == '-':
                codificar = codificar[1:]
        print(codificar)
        print("\n")
    elif opc_usuario == '2':
        numeros = input('ingrese el mensaje que desea decodificar (añada (-) entre los numeros): ')
        lista_numeros2 = list(numeros.split("-"))
        for numero in lista_numeros2:
            for numerito in lista_numeros:
                if numero == str(numerito):
                    letra = abc[lista_numeros.index(int(numero))]
                    decodificar += letra
        print(decodificar)
        print("\n")
    elif opc_usuario == '3':
        palabra_contar = input('ingrese la palabra que desea contar la frecuencia: ')
        for contar in palabra_contar:
            for conteo in range(len(abc)):
                if palabra_contar == abc[conteo]:
                    contar

        
