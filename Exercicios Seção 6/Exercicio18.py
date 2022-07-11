numeros_lidos = int(input('Informe a quantidade de numeros que devem ser verificados: '))
maior = 0

# Loop para determinar que o usuario precisa inserir a quantidade de numeros maior que 0
while numeros_lidos < 0:
    print('A quantidade informada é invalida')
    numeros_lidos = int(input('Informe a quantidade de numeros que devem ser verificados: '))

# Loop para determinar o maior numero informado e quantas vezes ele foi inserido
for i in range(0, numeros_lidos):
    numero = int(input('Numero: '))

    if numero > maior:
        maior = numero
        quant_n_maior = 1

    elif numero == maior:
        quant_n_maior += 1

print(f'\nMaior numero informado: {maior}\nQuantidade de vezes que ele foi informado: {quant_n_maior}')
