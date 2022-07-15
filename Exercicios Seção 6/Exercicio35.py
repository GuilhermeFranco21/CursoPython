inicial = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))

soma = 0

while inicial > final:
    print('\nIntervalo de valores invalido')
    inicial = int(input('Digite o valor inicial: '))
    final = int(input('Digite o valor final: '))

for i in range(inicial, final):
    if i % 2 != 0:
        soma += i

print(f'\nSoma dos impares nesse intervalo: {soma}')
