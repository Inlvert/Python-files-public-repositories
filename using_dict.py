# 'ab' - сокращение от 'a' dress 'b' ook
ab = { 'Swaroop'   : 'swaroop@swaroopch.com', 
       'Larry'     : 'larry@wall.org', 
       'Matsumoto' : 'matz@ruby-lang.org', 
       'Spammer'   : 'spammer@hotmail.com' }

print("Адрес Swaroop'a:", ab ['Swaroop'])
# Удаление пары ключ-значение
del ab['Spammer']

print('\nВ адресной книге {0} контакт\n'.format(len(ab)))
for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавляем пары ключ-значение
ab['Guido'] = 'guido@python.ogr'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])
    