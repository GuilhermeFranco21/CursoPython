preco_antigo = float(input('Digite o preço do produto: '))

if preco_antigo <= 50:
    preco_novo = preco_antigo + preco_antigo * 0.05
    print(f'Novo preço é de R${preco_novo}')

    print('Barato')
elif 50 < preco_antigo < 100:
    preco_novo = preco_antigo + preco_antigo * 0.10
    print(f'Novo preço é de R${preco_novo}')

    if 80 < preco_novo <= 120:
        print('Normal')
    elif preco_novo <= 80:
        print('Barato')

elif preco_antigo > 100:
    preco_novo = preco_antigo + preco_antigo * 0.15
    print(f'Novo preço é de R${preco_novo}')

    if 80 < preco_novo <= 120:
        print('Normal')

    elif 120 < preco_novo <= 200:
        print('Caro')

    elif preco_novo > 200:
        print('Muito Caro')
