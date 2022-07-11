data = input('Informe uma data (dd/mm/aaaa): ')
data2 = data.split('/')

dia = int(data2[0])
mes = int(data2[1])
ano = int(data2[2])

# Verificação de ano bissexto
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    # fevereiro
    if mes == 2:
        if 1 <= dia <= 29:
            print(f'{dia}/{mes}/{ano} é uma data valida')
        else:
            print(f'{dia}/{mes}/{ano} é uma data invalida')

if 1 <= mes <= 12:
    # janeiro, março, maio, julho, agosto, outubro e dezembro
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if 1 <= dia <= 31:
            print(f'{dia}/{mes}/{ano} é uma data valida')
        else:
            print(f'{dia}/{mes}/{ano} é uma data invalida')

    # abril, junho, setembro e novembro
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if 1 <= dia <= 30:
            print(f'{dia}/{mes}/{ano} é uma data valida')
        else:
            print(f'{dia}/{mes}/{ano} é uma data invalida')

    if mes == 2:
        if 1 <= dia <= 28:
            print(f'{dia}/{mes}/{ano} é uma data valida')
        else:
            print(f'{dia}/{mes}/{ano} é uma data invalida')
