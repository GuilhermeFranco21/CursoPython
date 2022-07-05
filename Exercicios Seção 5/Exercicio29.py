nome = input('Nome: ')
certas = 0

#Questão 1
print('1 - Quanto é 2 + 2?')
resposta1 = int(input('Resposta: '))

#Questão 2
print('2 - Quanto é 5 + 3?')
resposta2 = int(input('Resposta: '))

#Questão 3
print('3 - Quanto é 23 + 40?')
resposta3 = int(input('Resposta: '))

#Questão 4
print('4 - Quanto é 19 + 18?')
resposta4 = int(input('Resposta: '))

#Questão 5
print('5 - Quanto é 88 + 12?')
resposta5 = int(input('Resposta: '))

print('\n Prova corrigita')

if resposta1 == 4:
    print(f'1 - Quanto é 2 + 2? \nResposta: {resposta1} \nResposta correta: 4 \nSua resposta está correta')
    certas = certas + 1
else:
    print(f'1 - Quanto é 2 + 2? \nResposta: {resposta1} \nResposta correta: 4 \nsua resposta está errada')

if resposta2 == 8:
    print(f'2 - Quanto é 5 + 3? \nResposta: {resposta2} \nResposta correta: 8 \nSua resposta está correta')
    certas = certas + 1
else:
    print(f'2 - Quanto é 5 + 3? \nResposta: {resposta2} \nResposta correta: 8 \nsua resposta está errada')

if resposta3 == 63:
    print(f'3 - Quanto é 23 + 40? \nResposta: {resposta3} \nResposta correta: 63 \nsua resposta está correta')
    certas = certas + 1
else:
    print(f'3 - Quanto é 23 + 40? \nResposta: {resposta3} \nResposta correta: 63 \nsua resposta está errada')

if resposta4 == 37:
    print(f'4 - Quanto é 19 + 18? \nResposta: {resposta4} \nResposta correta: 37 \nsua resposta está correta')
    certas = certas + 1
else:
    print(f'4 - Quanto é 19 + 18? \nResposta: {resposta4} \nResposta correta: 37 \nsua resposta está errada')

if resposta5 == 100:
    print(f'5 - Quanto é 88 + 12? \nResposta: {resposta5} \nResposta correta: 100 \nsua resposta está correta')
    certas = certas + 1
else:
    print(f'5 - Quanto é 88 + 12? \nResposta: {resposta5} \nResposta correta: 100 \nsua resposta está errada')

print(f'\nVocê acertou um total de {certas}/5 perguntas')
