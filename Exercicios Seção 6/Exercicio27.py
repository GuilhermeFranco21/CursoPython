# Entrada de dados pelo usuario
numero = int(input('Digite um numero inteiro positivo: '))

h = 0

# Loop para determinar se o numero informado pelo usuario é positivo
while numero < 0:
    print('\nO numero informado é invalido')
    numero = int(input('Digite um numero inteiro positivo: '))

# Loop para determinar o valor de Hn
for i in range(1, numero+1):
    h = h + 1/i

print(f'\n H({numero}) = {h:,.2f}')

