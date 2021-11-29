import os
import glob
import sys
from main import DIR_XLSX


def cleaning_dir_xlsx():

    removing_files = glob.glob(DIR_XLSX + '//' + '*')

    if removing_files:
        print(f'Удаляю файлы из {DIR_XLSX}')
        for file in removing_files:
            os.remove(file)

    if glob.glob(DIR_XLSX + '//' + '*'):
        sys.exit('Ошибка: не все файлы удалены!')
