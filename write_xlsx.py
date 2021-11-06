
import os
import openpyxl
from datetime import datetime

import check_dbfs
import check_xlsx

print(os.getcwd())

filename_xlsx = f'СводДоходов_Ульяновск_{check_dbfs.month1[:-4]}.xlsx'

wb = openpyxl.Workbook()
ws1 = wb.create_sheet(title='Подразделения')
ws2 = wb.create_sheet(title='Регион')
wb.remove(wb['Sheet'])
NAME_HEAD = 'Свод доходов по Ульяновскому региону'


ws1['A1'] = NAME_HEAD
ws1['A2'] = 'В разрезе подразделений'
ws1['A3'] = datetime.now()


ws2['A1'] = NAME_HEAD
ws2['A2'] = 'По региону'
ws2['A3'] = datetime.now()

print('Запись файла')
wb.save(filename_xlsx)
