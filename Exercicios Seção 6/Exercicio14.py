numero = int(input('Digite um numero inteiro positivo: '))

while not(numero % 2 == 0):
    print('\nO numero informado é invalido')
    numero = int(input('Digite um numero inteiro positivo: '))

if numero % 2 == 0:
    for i in range(numero, 0-1, -1):
        print(i)
