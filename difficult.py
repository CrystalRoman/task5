def syst(n, s): #перевод в разные системы счисления
    ch = ''
    while n > 0:
        ch = str(n % s) + ch
        n //= s
    return ch

maxs = 0
res = 0
for n in range(1, 101):
    proms = 0
    for i in range(2, 10): #перебор оснований систем счисления
        ch = syst(n, i)
        for j in ch: #сумма цифр каждого числа => в общую сумму
            proms += int(j)
    if proms > maxs: #третье условие задачи
        maxs = proms
        res = n
print(res)
