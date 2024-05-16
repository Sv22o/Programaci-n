numero_1 = int(input('Ingrese un número:  '))
if numero_1 > 100:
    print('El número es mayor que 100')
elif numero_1 < 0:
    print('El número es negativo')
elif numero_1 % 2 == 0 and numero_1 % 3 == 0:
    print('El número es divisible por 6')
elif numero_1 % 2 == 0:
    print('El número es divisible por 2')
elif numero_1 % 3 == 0:
    print('El número es divisible por 3')
else:
    print('El número no cumple ninguna condición especial')