numero = int(input('Digite um numero inteiro positivo: '))
soma = 0

# Loop para determinar se o numero informado é positivo
while numero < 0:
    print('O numero informado é invalido')

# Loop para gerar os divisores e fazer a soma dos divisores
for i in range(1, numero):
    if numero % i == 0:
        soma += i
        print(i, end=', ')

print(f'\nA soma dos divisores do numero informado é: {soma}')
