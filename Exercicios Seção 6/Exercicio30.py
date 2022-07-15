numero = int(input('Digite um numero inteiro positivo: '))

soma1 = 0
soma2 = 0
soma3 = 0

for i in range(numero+1):
    soma1 += i
    if i % 2 == 0:
        soma2 -= i
    if i % 2 != 0:
        soma3 += i

print(f'Soma 1: {soma1} \nSoma 2: {soma2} \nSoma 3: {soma3}')
