km = int(input('Km percorridos: '))
litros = int(input('Quantidade de litros consumidos: '))

km_porl = km / litros

if km_porl < 8:
    print('Venda o carro!')

elif km_porl >= 8 and km_porl <= 14:
    print('Econômico!')

elif km_porl > 12:
    print('Super Econômico')
