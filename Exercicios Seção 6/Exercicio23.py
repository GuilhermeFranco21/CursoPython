numero = int(input('Digite um numero inteiro positivo: '))

# Verificação para validar se o numero informado é positivo
if numero > 0:
    print(f'Os divisores de {numero} são:')
else:
    print('O numero informado precisa ser positivo')

# Loop para determinar os divisores de "numero"
for i in range(1, numero+1):
    if numero % i == 0:
        print(i, end=', ')
