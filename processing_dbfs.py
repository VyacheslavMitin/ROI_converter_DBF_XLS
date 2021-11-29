
from read_dbfs import dbfs_append

USLUGI_NAMES = {
    '911': 'Обработка проинкассированных наличных денег',
    '133': 'Перевозка наличных денег по ден. чеку и объявлению на взнос наличными',
    '1': 'Инкассация',
    '77': 'Перевозка ценностей кредитных организаций',
    '23': 'Инкассация объектов топливно-заправочного комплекса',
    '900': 'Обслуживание банкоматов кредитных организаций',
    '455': 'Обслуживание терминалов кредитных организаций',
    '117': 'Перевозка разменной монеты ',
    '7': 'Доставка  ценностей кредитных организаций',
    '22': 'Инкассация объектов железной дороги ',
}

LIST_DICT_ALL_KODUSL = []  # услуга по коду
DICT_RECORDS = {}  # словарь для циклов


for record in dbfs_append()[2]:
    DICT_RECORDS.update(record)
    for key, value in DICT_RECORDS.items():  # создание списка с услугами
        if key == 'KODUSL':
            LIST_DICT_ALL_KODUSL.append(value)

dct_obem = {}  # словарь для объема
dct_vir = {}  # словарь для выручки
set_list = set(LIST_DICT_ALL_KODUSL)
dct_obem = dct_obem.fromkeys(set_list, 0)
dct_vir = dct_vir.fromkeys(set_list, 0)
print(dct_obem)
print(dct_vir)
print(DICT_RECORDS)

for record in dbfs_append()[2]:
    DICT_RECORDS.update(record)
    for key, value in dct_obem.items():
        for keys_, values_ in DICT_RECORDS.items():
            if values_ == key:
                dct_obem[key] += DICT_RECORDS.get('OBEM')

print(dct_obem)

dct_obem_rounded = {}
for key, value in dct_obem.items():
    dct_obem_rounded[key] = round(value, 2)

dct_obem_rounded_named = {}
for key, value in dct_obem_rounded.items():
    for keys_, values_ in USLUGI_NAMES.items():
        if key == keys_:
            dct_obem_rounded_named[values_] = value


for record in dbfs_append()[2]:
    DICT_RECORDS.update(record)
    for key, value in dct_vir.items():
        for keys_, values_ in DICT_RECORDS.items():
            if values_ == key:
                dct_vir[key] += DICT_RECORDS.get('VIR')

dct_vir_rounded = {}
for key, value in dct_vir.items():
    dct_vir_rounded[key] = round(value, 2)

print(dct_vir)
print(dct_vir_rounded)

dct_vir_rounded_named = {}
for key, value in dct_vir_rounded.items():
    for keys_, values_ in USLUGI_NAMES.items():
        if key == keys_:
            dct_vir_rounded_named[values_] = value


dct_vir_rounded_named_nds = {}
for key, value in dct_vir_rounded_named.items():
    dct_vir_rounded_named_nds[key] = round((value * 1.2), 2)

print("\nДанные для эксель")
print('Объем:', dct_obem_rounded_named)
print('Доход:', dct_vir_rounded_named)
print('Доход с НДС:', dct_vir_rounded_named_nds)

