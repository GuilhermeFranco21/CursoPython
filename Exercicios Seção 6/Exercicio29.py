s = 0
fatorial = 1
fatorial2 = 0
numerador = 0

for i in (2, 6, 2):
    fatorial = fatorial * i
    fatorial2 = fatorial2 + fatorial
    numerador += 1
    s +=  numerador / fatorial2

print(s)