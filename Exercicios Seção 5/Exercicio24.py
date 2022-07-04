estado = int(input(' [1] - MG \n [2] - SP \n [3] - RJ \n [4] - MS \nSelecione um Estado: '))
preço = float(input('Preço do produto: '))

while estado < 1 or estado > 4:
    print('Selecione um Estado valido')
    estado = int(input(' [1] - MG \n [2] - SP \n [3] - RJ \n [4] - MS \nSelecione um Estado: '))

if estado == 1:
    preço_final = preço + (preço * 0.07)
    print(f'Preço final para o Estado de Minas Gerais: R${preço_final}')

elif estado == 2:
    preço_final = preço + (preço * 0.12)
    print(f'Preço final para o Estado de São Paulo: R${preço_final}')

elif estado == 3:
    preço_final = preço + (preço * 0.15)
    print(f'O preço final para o Estado do Rio de Janeiro: R${preço_final}')

elif estado == 4:
    preço_final = preço + (preço * 0.08)
    print(f'O preço final para o Estado do Mato Grosso do Sul: R${preço_final}')
