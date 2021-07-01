def printMax(x, y):
    '''вывод максимальное из двух чисел.
    оба значения должны быть целыми числами.'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'наибольшое')
    else:
        print(y, 'наибольшое')
printMax(3, 5)
print(printMax.__doc__)

