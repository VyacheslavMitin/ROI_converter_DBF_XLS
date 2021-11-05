# Модуль работы для чтения DBF файла и поготовки таблицы в экселе
# Установить: pysimplegui, xlwt, dbfread, openpyxl
import PySimpleGUI as sg
import xlwt
import dbfread
import openpyxl

layout = [
    [sg.Text('Необходимо выбрать три файла DBF по подразделениям')],
    [sg.Text('')],
    [sg.FileBrowse(file_types=("DBF файл", "*.dbf"), button_text="Файл..."),
     sg.Text('Касса пересчета Ульяновска 63053_ХХ.dbf')],
    [sg.FileBrowse(file_types=("DBF файл", "*.dbf"), button_text="Файл..."),
     sg.Text('Ульяновский участок 63054_ХХ.dbf')],
    [sg.FileBrowse(file_types=("DBF файл", "*.dbf"), button_text="Файл..."),
     sg.Text('Димитровградский участок 63055_ХХ.dbf')],
    [sg.Text('')],
    [sg.Text('Результат:', size=(10, 1)), sg.Input(key='-output-')],
    [sg.Text('')],
    [sg.Button('Генерация отчета'), sg.Button('Подготовка письма'), sg.Button('Выход')]
]

window = sg.Window('Отчет по выручке для Самары', layout)  # создание окна

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
