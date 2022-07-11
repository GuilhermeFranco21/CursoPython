for i in range(1, 4):
    numero = int(input('Digite um numero inteiro: '))

    if i == 1:
        maior = numero
        menor = numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(f'O mairo numero informado foi {maior} e o menor numero informado foi {menor}')

