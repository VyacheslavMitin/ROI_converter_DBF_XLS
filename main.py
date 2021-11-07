# Модуль работы для чтения DBF файла и поготовки таблицы в экселе
# Установить: pysimplegui, dbfread, openpyxl
import os
import sys

PATH_MODULE: str = os.path.abspath(os.path.dirname(__file__))
DIR_DBFS: str = os.path.join(PATH_MODULE, 'dbfs')
DIR_XLSX: str = os.path.join(PATH_MODULE, 'xlsx')



