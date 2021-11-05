# Импортировать модуль
import dbfread
import xlwt

dbf_filename = '63053_10.DBF'
xls_filename = dbf_filename.lower().replace('dbf', 'xls')
# Имя файла таблицы данных
table = dbfread.DBF(dbf_filename, encoding='cp866')
all_sheet = []
book = xlwt.Workbook()  # Создать новый Excel
sheet = book.add_sheet('all_sheet')  # Добавить страницу листа
row = 0  # Контролировать количество строк
write_row = 0
sheet_list = []
for record in table:
    col = 0
    if not all_sheet:  # Это только один раз читает имя поля для управления
        sheet_dict = record.keys()
        # print(type(sheet_dict))         # <class 'odict_keys'>
        sheet_list = list(set(sheet_dict))  # Преобразовать odict_keys в список для работы
        all_sheet = sheet_list
    if write_row == 0:  # Напишите имя поля только один раз, чтобы управлять
        col = 0
        for i in range(len(sheet_list)):
            sheet.write(row, col, sheet_list[i])
            col += 1
        col = 0
        row += 1
        write_row += 1
    for field in record:
        sheet.write(row, col, record[field])
        # print(field,'=',record[field],end='')
        col += 1
    row += 1


book.save(xls_filename)  # Сохранить в указанный файл в указанном каталоге
