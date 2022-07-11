chegada = input('Hora de chegada separada por ":": ')
saida = input('Hora de saída separada por ":": ')

chegada2 = chegada.split(':')
saida2 = saida.split(':')

hora_saida = saida2[0] + saida2[1]
hora_saida = int(hora_saida)

hora_chegada = chegada2[0] + chegada2[1]
hora_chegada = int(hora_chegada)

tempo_decorrido = (hora_chegada - hora_saida) * -1
print(tempo_decorrido)
if 100 <= tempo_decorrido <= 200:
    print(f'Valor a pagar: R${(tempo_decorrido/100)*1}')
