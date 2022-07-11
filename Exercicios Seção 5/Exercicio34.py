nota = float(input('Nota: '))
faltas = int(input('Faltas: '))


if 9 <= nota <= 10 and faltas <= 20:
    print('A')

elif 9 <= nota <= 10 and faltas > 20:
    print('B')


elif 7.5 <= nota <= 8.9 and faltas <= 20:
    print('B')

elif 7.5 <= nota <= 8.9 and faltas > 20:
    print('C')


elif 5 <= nota <= 7.4 and faltas <= 20:
    print('C')

elif 5 <= nota <= 7.4 and faltas > 20:
    print('D')


elif 4 <= nota <= 4.9 and faltas <= 20:
    print('D')

elif 4 <= nota <= 4.9 and faltas > 20:
    print('E')


elif 0 <= nota <= 3.9 and faltas > 20:
    print('E')

elif nota < 0 or nota > 10:
    print('A nota informada é invalida')

if faltas < 0:
    print('Numero de faltas informadas é invalida')
