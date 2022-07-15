for i in range(1000, 9999 + 1):
    # Separando string
    i = str(i)
    a = i[0:2]
    b = i[2:4]

    # convertendo
    a = int(a)
    b = int(b)
    i = int(i)
    # calculando
    c = a + b

    if c ** 2 == i:
        print(i)
