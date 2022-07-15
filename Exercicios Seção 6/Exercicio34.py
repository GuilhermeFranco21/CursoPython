n1 = 1
n2 = 1
while n2 <= 20:
    if n1 % n2 == 0:
        n2 = n2 + 1
    else:
        n1 = n1 + 1
        n2 = 1
print(n1)