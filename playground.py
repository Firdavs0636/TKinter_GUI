def add(*args):
    summa = 0
    # summa = sum(args)
    # return summa
    for i in args:
        summa += i + 1
    return summa


result = add(2, 3, 4, 5)
print(result)
