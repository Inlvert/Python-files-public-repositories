# Это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'банан']
print('Я должен сделать', len(shoplist), 'покупки')

print('Покупки: ', end=' ')
for item in shoplist:
    print(item, end=' ')
print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('теперь мой список покупок таков: ', shoplist)
print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)

print('первое что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('я купил', olditem)
print('теперь мой список покупок:', shoplist)
