def total(inital=5, *numbers, extra_number):
    count = inital
    for number in numbers:
        count += number
    count += extra_number
    print(count)
total(10, 1, 2, 3, extra_number=50)
total(10, 1, 2, 3)
#вызовет ошибку, поскольку мы не указали значения
#аргумент поумолчанию да 'extra_nuber'.