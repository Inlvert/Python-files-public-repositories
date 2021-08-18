import pickle
# Имя файла в котором мы сохраним объект
shoplistlile = 'shoplist.data'
# список пуст
shoplist = ['яблки','морковь','манго']

# запись файла

f = open(shoplistlile, 'wb')
pickle.dump(shoplist, f) # Помещаем объект в файл
f.close()

del shoplist # Уничтожаем переменную shoplist

# считываем из хранилища
f = open(shoplistlile, 'rb')
storedlist = pickle.load(f) # загружаем объект из файла
print(storedlist)