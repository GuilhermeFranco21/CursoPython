a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))


if a == 0:
    print('Não é uma equação do segundo grau')

else:
    delta = (b**2) - (4 * a * c)
    raiz1 = (-b + pow(delta,0.5)) / (2*a)
    raiz2 = (-b - pow(delta,0.5)) / (2*a)

    if delta < 0:
        print('Não existe raiz')

    elif delta == 0:
        print(f'{raiz1} Raiz unica')

    else:
        print(f'R1: {raiz1}' f'\nR2: {raiz2}')

