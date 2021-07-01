def total(a=5, *numbers, **phonebook):
    print("a", a)
    #проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)
    #проход по всем элементам словаря
    for firs_part, second_part in phonebook.items():
        print(firs_part, second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

