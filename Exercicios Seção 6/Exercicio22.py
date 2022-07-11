contador = 0
soma = 0
nota = float(input('informe a primeira nota entre 10 e 20: '))

while 10 < nota < 20:
    nota = float(input('\nNota: '))
    if 10 < nota < 20:
        contador += 1
        soma = soma + nota

media = soma / contador
print(f'Media das {contador} notas: {media}')
