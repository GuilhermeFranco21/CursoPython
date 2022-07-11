venda = float(input('Venda mensal: '))

if 5000 <= venda < 20000:
    comissao = venda * 0.14 + 400
    print(f'Comissão do vendedor: R${comissao:,.2f}')

if 20000 <= venda < 40000:
    comissao = venda * 0.14 + 500
    print(f'Comissão do vendedor: R${comissao:,.2f}')

if 40000 <= venda < 60000:
    comissao = venda * 0.14 + 550
    print(f'Comissão do vendedor: R${comissao:,.2f}')

if 60000 <= venda < 80000:
    comissao = venda * 0.14 + 600
    print(f'Comissão do vendedor: R${comissao:,2.f}')

if 80000 <= venda < 100000:
    comissao = venda * 0.14 + 650
    print(f'Comissão do vendedor: R${comissao:,.2f}')

if 100000 <= venda:
    comissao = venda * 0.16 + 700
    print(f'Comissão do vendedor: R${comissao:,.2f}')

if venda < 5000:
    print('Comissão do vendedor: R$00.00')

