numero = int(input('Digite um numero: '))

# Loop para determinar o primeiro multiplo de 11, 13 ou 17 ápos um determinado número inserido pelo usuario
while True:
    numero += 1
    if numero % 11 == 0 or numero % 13 == 0 or numero % 17 ==0:
        print(numero)
        break
