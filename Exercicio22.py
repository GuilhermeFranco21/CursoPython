idade = int(input('Idade: '))
tempo_serviço = int(input('Tempo de serviço em anos: '))
diferença = 0
diferença2 = 0

if idade >= 65 or tempo_serviço >= 30:
    print('Já é possível se aposentar')

elif idade >= 60 and tempo_serviço >=25:
    print('Já é possível se aposentar')

else:
    while idade < 60:
        idade = idade + 1
        diferença = diferença + 1

    if tempo_serviço < 25:
        while tempo_serviço < 25:
            tempo_serviço = tempo_serviço +1
            diferença2 = diferença2 + 1

        else:
            tempo_total = diferença + diferença2
            if diferença > diferença2:
                print(f'Você ainda precisa trabalhar mais {diferença} anos')
            else:
                print(f'Você ainda precisa trabalhar por mais {tempo_total} anos')
