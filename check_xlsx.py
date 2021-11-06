import os
import glob
import sys
import read_dbfs

XLSX_DIR = os.path.join('xlsx')
os.chdir(XLSX_DIR)
print(os.getcwd())

files = glob.glob('*')
print(files)
if files:
    print('Удаляю файлы')
    for file in files:
        os.remove(file)

if glob.glob('*'):
    sys.exit('Ошибка: не все файлы удалены!')
