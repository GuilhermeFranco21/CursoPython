teste = True

while teste:
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    if a < b < c:
                        print(f'a = {a} b = {b} c = {c} ')
                        teste = False
