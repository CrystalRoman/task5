def f(A, x):
    return ((72 % x == 0) <= (not (120 % x == 0))) or (A - x > 100) #условие

for A in range(-200,200):
    for x in range(1,200): 
        if not f(A, x): #если хотя бы один Х не даёт правду, то такое А не подходит
            break
    else: #если все Х подошли
        print(A)
        break #так как нужно мин A, то выходим из цикла
