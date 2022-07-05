nota = float(input('Nota: '))
faltas = int(input('Faltas: '))

if 9 <= nota <= 10 and faltas <= 20:
    print('A')
    if faltas > 20:
        print('B')

elif 7.5 <= nota <= 8.9 and faltas <=20:
    print('B')
    if faltas > 20:
        print('C')