
import os
import glob
import sys
from main import DIR_DBFS

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


def checking_dbfs() -> list:
    os.chdir(DIR_DBFS)
    dbfs_files_lower = glob.glob('*.DBF')
    if dbfs_files_lower:
        for files in dbfs_files_lower:
            file, _ = dbfs_files_lower[0].split('.')
            os.rename(files, f'{file}.dbf')
    dbfs_files = glob.glob('*.dbf')
    dbfs_files.sort()

    if len(dbfs_files) != 3:
        sys.exit('Ошибка: количество файлов отличается от трех штук!')
    else:
        print('Три файла, все хорошо')

    subdivisions, months = [], []
    for files in dbfs_files:
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

    return dbfs_files


# checking_dbfs()
