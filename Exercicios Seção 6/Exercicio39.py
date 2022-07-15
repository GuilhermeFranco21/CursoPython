base = int(input('Digite o comprimento da base do triangulo: '))
altura = int(input('Digite o comprimento da altura do triangulo: '))

area_triangulo = (base * altura) / 2

while altura <= 0 or base <= 0:
    print('Os valores informados precisam ser maiores do que 0')
    base = int(input('\nDigite o comprimento da base do triangulo: '))
    altura = int(input('Digite o comprimento da altura do triangulo: '))

if altura and base > 0:
    print(f'A area do tringulo é igual a ({base} * {altura}) / 2 = {area_triangulo}')
