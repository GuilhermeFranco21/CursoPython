altura = float(input('Informe sua altura: '))
peso = float(input('Informe o seu peso: '))

#Altura até 1.20
if altura < 1.20 and peso <= 60:
    print('Classificação A')

elif altura < 1.20 and 60 >= peso <= 90:
    print('Classificação D')

elif altura < 1.20 and peso > 90:
    print('Classificação G')

#Altura de 1.20 até 1.70
if 1.20 <= altura < 1.70 and peso <= 60:
    print('Classificação B')

elif 1.20 <= altura < 1.70 and 60 >= peso <= 90:
    print('Classificação E')

elif 1.20 <= altura < 1.70 and peso > 90:
    print('Classificação H')

#Altura maior do que 1.70
if altura > 1.70 and peso <= 60:
    print('Classificação C')

elif altura > 1.70 and 60 < peso <= 90:
    print('Classificação F')

elif altura > 1.70 and peso > 90:
    print('Classificação I')

else:
    print('Não será possível fazer a sua classificação')
