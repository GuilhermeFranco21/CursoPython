numero = int(input('Digite um numero inteiro positivo par: '))

while not(numero % 2) == 0:
    print('\nO numero informado não é permitido')
    numero = int(input('Digite um numero inteiro positivo par: '))

if numero % 2 == 0:
    for i in range(0, numero+1, 2):
        if numero % 2 == 0:
                print(i)
