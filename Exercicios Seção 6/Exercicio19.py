# Programa para imprimir os algarismos de um numero informado pelo usuario
numero_str = input('Informe um numero entre 100 e 999: ')
numero_int = int(numero_str)

# Fazendo uso de loop
while not(100<=numero_int<=999):
    print('\nO numero informado não está entre 100 e 999')
    numero_str = input('Informe um numero entre 100 e 999: ')
    numero_int = int(numero_str)

if 100 <= numero_int <= 999:
    for i in numero_str:
        print(i, end=' ')

# Fazendo uso de slice de string
print(numero_str[0], numero_str[1], numero_str[2])
