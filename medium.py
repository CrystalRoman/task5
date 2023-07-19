def troy(n): #построение троичной записи числа
    ch = ''
    while n > 0:
        ch = str(n % 3) + ch
        n //= 3
    return ch

maxr = 0
for n in range(1, 10000):
    n3 = troy(n)
    k0 = n3.count('0') #кол-во нулей
    k1 = n3.count('1') #кол-во единиц
    n3 = str((k0 + k1) % 3) + n3 #приписываем остаток
    r = int(n3, 3)
    if r < 1000:
        maxr = max(maxr, r)
print(maxr)
