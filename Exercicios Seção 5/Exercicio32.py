# Menu da lanchonete
print(' Especificações    Código    Preço \n Cachorro Quente     100      1.20'
      '\n Bauru Simples       101      1.30 \n Bauru com Ovo       102      1.30 \n Hamburguer          103      1.50'
      '\n Cheseburguer        104      1.20 \n Suco                105      1.70'
      '\n Refrigerante        106      2.20')

# Escolha do cliente e quantidade
codigo = int(input('\nDigite o código do iten desejado: '))
quantidade = int(input('Digite a quantidade desejada: '))

# Execução
if codigo == 100:
    preço_final = quantidade * 1.20
    print(f'Seu pedido de {quantidade} Cachorro Quente ficou em' f' R${preço_final:,.2f}')

if codigo == 101:
    preço_final = quantidade * 1.30
    print(f'Seu pedido de {quantidade} Bauru Simples ficou em' f' R${preço_final:,.2f}')

elif codigo == 102:
    preço_final = quantidade * 1.30
    print(f'Seu pedido de {quantidade} Bauru com Ovo ficou em' f' R${preço_final:,.2f}')

elif codigo == 103:
    preço_final = quantidade * 1.50
    print(f'Seu pedido de {quantidade} Hamburguer ficou em' f' R${preço_final:,.2f}')

elif codigo == 104:
    preço_final = quantidade * 1.20
    print(f'Seu pedido de {quantidade} Cheseburguer ficou em' f' R${preço_final:,.2f}')

elif codigo == 105:
    preço_final = quantidade * 1.70
    print(f'Seu pedido de {quantidade} Suco ficou em' f' R${preço_final:,.2f}' )

elif codigo == 106:
    preço_final = quantidade * 2.20
    print(f'Seu pedido de {quantidade} Refrigerante ficou em' f' R${preço_final:,.2f}')

else:
    print('O código inserido é invalido')
