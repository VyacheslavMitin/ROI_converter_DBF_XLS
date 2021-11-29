
from read_dbfs import dbfs_append

USLUGI = {
    '911': 'Обработка проинкассированных наличных денег',
    '133': 'dfdfd',
    '1': 'dfdfd',
    '77': 'dfdfd',
    '23': 'dfdfd',
    '900': 'dfdfd',
    '455': 'dfdfd',
    '117': 'dfdfd',
    '7': 'dfdfd',
    '22': 'dfdfd',
}

LIST_DICT_ALL_KODUSL = []  # услуга по коду
LIST_DICT_ALL_OBEM = []  # объем
LIST_DICT_ALL_VIR = []  # выручка
DICT_RECORDS = {}  # словарь для циклов

LIST_test = []
DICT_test = []
dct = {}

for record in dbfs_append()[2]:
    DICT_RECORDS.update(record)
    # print(DICT_RECORDS)
    # dct = {}
    # for k, v in slovari.items()
    #     if k in dct:
    #         dct[k] += v
    #     else:
    #         dct[k] = v
    for key, value in DICT_RECORDS.items():  # создание списка с услугами
        if key == 'KODUSL':
            # print(value)
            LIST_DICT_ALL_KODUSL.append(value)
            # if value in dct:
            #     dct[key] += value
            # else:
            #     dct.update(value=DICT_RECORDS.get('VIR'))
                # dct.fromkeys([value], DICT_RECORDS.get('VIR'))
                # dct[key] = value

set_list = set(LIST_DICT_ALL_KODUSL)
dct = dct.fromkeys(set_list, 0)
print(dct)
print(DICT_RECORDS)


for record in dbfs_append()[2]:
    DICT_RECORDS.update(record)
    for key, value in dct.items():
        for keys_, values_ in DICT_RECORDS.items():
            if values_ == key:
                dct[key] += DICT_RECORDS.get('VIR')


print(dct)


