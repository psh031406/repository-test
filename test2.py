p = []

for n in range(2, 101):
    is_p = True
    for i in range(2, n):
        if n % i == 0:
            is_p =False
    if is_p:
        p.append(n)

print('2에서 100사이의 소수들:', p)
