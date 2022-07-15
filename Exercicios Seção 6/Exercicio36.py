soma = 0
soma_quadrados = 0

for i in range(101):
    soma += i
    soma_quadrados += i ** 2

print(f'A diferença entre a soma do quadrado dos 100 primeiros numeros '
      f'\nnaturais e o quadrado da soma é: {soma ** 2} - {soma_quadrados} = {(soma**2) - soma_quadrados}')

