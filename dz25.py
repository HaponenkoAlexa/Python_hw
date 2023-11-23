from functools import partial

def pow(x, exp):
    return x ** exp

def some_gen(begin, end, func):
    """
    begin: перший елемент послідовності
    end: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    current = begin
    count = 0

    while count < end:
        yield current
        current = func(current)
        count += 1

from inspect import isgenerator

# Використовуйте partial, щоб передати тільки один аргумент для функції pow
gen = some_gen(2, 4, partial(pow, exp=2))
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
