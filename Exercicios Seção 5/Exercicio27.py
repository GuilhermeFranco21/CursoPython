idade = int(input('Idade do nadador: '))

if idade >= 5 and idade <= 7:
    print(f'A idade de {idade} é categoria Infantil A')

elif idade >= 8 and idade <= 10:
    print(f'A idade de {idade} é categoria Infantil B')

elif idade >= 11 and idade <= 13:
    print(f'A idade de {idade} é categoria Infantil C')

elif idade >= 14 and idade <= 17:
    print(f'A idade de {idade} é categoria Infantil D')

elif idade >= 18 and idade < 40:
    print(f'A idade de {idade} é categoria Sênior')

else:
    print(f'A idade de {idade} não está autorizada a nadar')