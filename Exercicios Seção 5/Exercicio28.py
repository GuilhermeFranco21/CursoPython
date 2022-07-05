operaçao = input(' Geométrica \n Ponderada \n Harmônica \n Aritimética \nSelecione uma das médias: ')

x = int(input('DIgite um numero inteiro positivo: '))
y = int(input('Digite outro numero inteiro positivo: '))
z = int(input('Digite outro numero inteiro positivo: '))

if x >= 0 and y >= 0 and z >= 0:
    if operaçao.lower() == "geométrica":
        geometrica = pow(x * y * z, 1/3)
        print(geometrica)

    elif operaçao.lower() == "ponderada":
        ponderada = (x + 2*y + 3*z) / 6
        print(ponderada)

    elif operaçao.lower() == "harmônica":
        harmonica = 1 / (1/x + 1/y + 1/z)
        print(harmonica)

    elif operaçao.lower() == "aritimética":
        aritimetica = (x + y + z) / 3

    else:
        print('Selecione uma média valida')
else:
    print('Os numeros precisam ser numeros inteiros positivos')
