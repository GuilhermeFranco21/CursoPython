import random

# Entrada de dados pelo usuario
start = input('Digite "Start" para rolar os dados: ')
start = start.lower()

# Verificador para determinar se entrada do usuario está de acordo com o pedido
while start != 'start':
    start = input('Digite "Start" para rolar os dados: ')
    start = start.lower()

if start == 'start':

    # loop para rolar os dados
    while start != 'stop':
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)

        # Comparador dos dados
        if dado1 > dado2:
            print(f'Primeiro dado: {dado1} \nSegundo dado: {dado2}')
            print(f'{dado1} > {dado2}')
        elif dado1 < dado2:
            print(f'Primeiro dado: {dado1} \nSegundo dado: {dado2}')
            print(f'{dado1} < {dado2}')
        if dado1 == dado2:
            print(f'Primeiro dado: {dado1} \nSegundo dado: {dado2}')
            print(f'{dado1} = {dado2}')


        start = input('Digite "Enter" para rolar os dados novamente ou "Stop" para finalizar: \n')
        start = start.lower()
