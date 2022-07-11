numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

soma = 0
multiplicacao = 1

# Loop para efetuar a multiplicação e soma dos numeros em ordem crescente
for i in range(numero1, numero2+1):
    if i % 2 != 0:
        multiplicacao = multiplicacao * i
    elif i % 2 == 0:
        soma += i

# Loop para efetuar a multiplicação e soma dos numeros em ondem decrescente
if numero1 > numero2:
    for i in range(numero1, numero2-1, -1):
        if i % 2 != 0:
            multiplicacao = multiplicacao * i
        elif i % 2 == 0:
            soma += i

print(f'Soma dos numeros do intervalo informado: {soma}\nMultiplicação dos numeros impares no intervalo informado:'
      f' {multiplicacao}')
