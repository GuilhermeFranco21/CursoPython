soma = 0

for n in range(3):
    if n >= 0:
        numero = int(input('Informe um numero intereiro positivo: '))
        soma = soma + numero
        media = soma / 10
    else:
        print('Os numeros informados são invalidos')
print(f'A média dos numeros informados é {media}')