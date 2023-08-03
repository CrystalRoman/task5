from functools import *

def m(h): #все возможные ходы
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 4, b), (a, b * 4)
@lru_cache(None)
def g(h):
    a, b = h
    if a + b >= 105: #выигрыш при условии камней >= 105
        return 'WIN'
    if any(g(x) == 'WIN' for x in m(h)):
        return 'P1' #Петя первым выиграл
    if all(g(x) == 'P1' for x in m(h)): #чтобы ответить на первый вопрос, необходимо all заменить на any и взять минимальное число, где есть W1 (выигрыш Вани)
        return 'W1' #Ваня первым выиграл
    if any(g(x) == 'W1' for x in m(h)):
        return 'P2' #ответ на второй вопрос (Петя вторым выиграл)
    if all(g(x) == 'P2' or g(x) == 'P1' for x in m(h)):
        return 'W2' #ответ на третий вопрос (Ваня первым или вторым выиграл)

for i in range(30, 1, -1): #перебираем вторую кучу
    h = 4, i #так легко передавать кучи вместе (упаковываем)
    a = g(h)
    if a != None: #для скрытия пустых значений
        print(i, a)
