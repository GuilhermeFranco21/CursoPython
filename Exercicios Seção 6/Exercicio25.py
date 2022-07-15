soma = 0

for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(f'A soma dos multiplos de 3 ou 5 em um intervalo de 0 a 1000 é: {soma}')
