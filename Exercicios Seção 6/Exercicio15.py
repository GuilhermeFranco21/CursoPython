numero = int(input('Digite um numero inteiro positivo impar: '))

while numero % 2 == 0:
    print('\nO numero informado é invalido')
    numero = int(input('Digite um numero inteiro positivo impar: '))

if not(numero % 2 == 0):
    for i in range(1, numero+1, 2):
        print(i)
