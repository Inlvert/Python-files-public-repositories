import os
import time
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в спиок.
source = ['"/home/inlvert/Python files public repositories"', '/home/inlvert/Pictures']
# для имен, содержащих пробелы, необходимо использовать двойные кавычки внутри строки
#2. Резервные копии должны хранится в основном каталоге резерва.
target_dir = '/home/inlvert/Backup_test'
# 3. Файли помещаются в ZIP-архив
# 4. текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# текущее время служит именем zip-архив
now = time.strftime('%H%M%S')
#Запрашиваем коминтарий пользователя для имени файла
comment = input('Введите коментарий -->')
if len(comment) == 0: #проверяем, введён ли коментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +
    comment.raplace(' ', '_') + '.zip'
# Создаем каталог, если такого ещё нет
if not os.path.exists(today):
    os.mkdir(today) # Создание каталога
    print('Каталог успешно создан', today)
# Имя Zip-файла
target = today + os.sep + now + '.zip'

# 5. Используем команду 'zip' для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
# Запускаем создание резервной копии
if os.system(zip_command) ==0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')