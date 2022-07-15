numero = int(input('Digite um numero inteiro positivo: '))

soma = 0
fatorial = 1
fatorial2 = 0

# Loop para verificação (numero positivo)
while numero < 0:
    print('O numero informado é invalido')
    numero = int(input('Digite um numero inteiro positivo: '))

# Loop para realizar a fatoração e o calculo da formula E
for i in range(1, numero+1):
    fatorial = fatorial * i
    fatorial2 = fatorial2 + (1 / fatorial)
    soma += fatorial2

print(f'A soma de E é: {soma:,.2f}')
