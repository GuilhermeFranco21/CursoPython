s = 0
denominador = 0
for i in range(1,101, 2):
    denominador += 1
    divisao = i / denominador
    s += divisao
print(s)