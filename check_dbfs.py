
import os
import glob
import sys

# MONTHS_DICT = {
#     '01.dbf': 'Январь',
#     '02.dbf': 'Февраль',
#     '03.dbf': 'Март',
#     '04.dbf': 'Апрель',
#     '05.dbf': 'Май',
#     '06.dbf': 'Июнь',
#     '07.dbf': 'Июль',
#     '08.dbf': 'Август',
#     '09.dbf': 'Сентябрь',
#     '10.dbf': 'Октябрь',
#     '11.dbf': 'Ноябрь',
#     '12.dbf': 'Декабрь',
#                }

DBFS_DIR = os.path.join('dbfs')
os.chdir(DBFS_DIR)
print(os.getcwd())
DBFS_FILES = glob.glob('*.dbf')
DBFS_FILES.sort()
print(DBFS_FILES)
if len(DBFS_FILES) != 3:
    sys.exit('Ошибка: количество файлов отличается от трех штук!')
else:
    print('Три файла, все хорошо')
a, b, c = DBFS_FILES
print(a, b, c)
subdivisions, months = [], []
for files in DBFS_FILES:
    subdivision, month = files.split('_')
    subdivisions.append(subdivision)
    months.append(month)

subdivision1, subdivision2, subdivision3 = subdivisions
month1, month2, month3 = months

if subdivision1 == '63053' and subdivision2 == '63054' and subdivision3 == '63055':
    print('Подразделения совпадают')
else:
    sys.exit('Ошибка: Подразделения не совпадают')

if month1 == month2 and month2 == month3:
    print('Месяца совпадают')
else:
    sys.exit('Ошибка: месяца не совпадают!')

