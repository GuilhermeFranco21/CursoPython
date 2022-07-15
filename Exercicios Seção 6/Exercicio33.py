"""
Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem
crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos.
"""
numero = int(input('Digite o valor de n: '))
i = int(input('Digite o valor de i: '))
j = int(input('Digite o valor de j: '))

for n in range(0, numero+1):
    if n % i == 0 or n % j == 0:
        print(n)
