import os
import time
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в спиок.
source = ['"/home/inlvert/Python files public repositories"', '/home/inlvert/Pictures']
# для имен, содержащих пробелы, необходимо использовать двойные кавычки внутри строки
#2. Резервные копии должны хранится в основном каталоге резерва.
target_dir = '/home/inlvert/Backup_test'
# 3. Файли помещаются в ZIP-архив
# 4. Именем для ZIP-архива служит текущая дата и время.
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# 5. Используем команду 'zip' для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
# Запускаем создание резервной копии
if os.system(zip_command) ==0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')