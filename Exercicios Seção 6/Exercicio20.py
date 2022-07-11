dados_lidos = 0
par = 0
numero = 0

while numero != 1000:
    numero = int(input('\nDigite um numero: '))
    dados_lidos += 1
    if numero % 2 == 0:
        print(f'O numero {numero} é par')
        par += 1
    elif not(numero%2==0):
        print(f'O numero {numero} é impar')

print(f'\nQuantidade de dados analizados: {dados_lidos}\nQuantidade de numeros pares analizados: {par}')
