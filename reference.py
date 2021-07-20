print('простое присваевание')
shoplist = ['яблоки', 'манго', 'морковь', 'банан']
mylist = shoplist # еще одно имя указывается на тот же объект!
del shoplist[0] # я сделал первую покупу поэтому удаляю ее из списка
print('shoplist:', shoplist)
print('mylist:', mylist)
# 
print('Копирование при помощи полной вырезки')
mylist = shoplist[:] # создаем копию путем полной вырезки
del mylist[0] # Удаляем первый элемент
print('shoplist:', shoplist)
print('mylist:', mylist) # теперь списки разные