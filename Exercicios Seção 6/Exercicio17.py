numero = int(input('Informe um numero inteiro positivo: '))
soma = 0

while numero < 0:
    print('\nO numero informado é invalido')
    numero = int(input('Informe um numero inteiro positivo: '))

for i in range(0, numero+1):
    soma = soma + i

print(f'A soma dos numeros naturais de 0 até {numero} é igual a {soma}')
