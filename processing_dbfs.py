
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

# print(dbfs_append())
# for tables in dbfs_append():
#     for record in tables:
#         DICT_RECORDS.update(record)
#         LIST_DICT_ALL_KODUSL.append(DICT_RECORDS.get('KODUSL'))
#         LIST_DICT_ALL_OBEM.append(DICT_RECORDS.get('OBEM'))
#         LIST_DICT_ALL_VIR.append(DICT_RECORDS.get('VIR'))

# for record in dbfs_append()[0]:
#     DICT_RECORDS.update(record)
#     LIST_DICT_ALL_KODUSL.append(DICT_RECORDS.get('KODUSL'))
#     LIST_DICT_ALL_OBEM.append(DICT_RECORDS.get('OBEM'))
#     LIST_DICT_ALL_VIR.append(DICT_RECORDS.get('VIR'))
# for record in dbfs_append()[1]:
#     DICT_RECORDS.update(record)
#     LIST_DICT_ALL_KODUSL.append(DICT_RECORDS.get('KODUSL'))
#     LIST_DICT_ALL_OBEM.append(DICT_RECORDS.get('OBEM'))
#     LIST_DICT_ALL_VIR.append(DICT_RECORDS.get('VIR'))
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
    for key, value in DICT_RECORDS.items():
        print(type(key))
        if key in dct:
            dct[key] += value
        else:
            dct[key] = value
print(dct)
    # for key, value in DICT_RECORDS.items():
    #     # print(key, value)
    #     for key_ in list(USLUGI.keys()):
    #         if (key, value) == ('KODUSL', key_):
    #             # print(key_, DICT_RECORDS.get('VIR'))
    #             LIST_test.append(DICT_RECORDS.get('VIR'))  # сумма обшая
    #             DICT_test.append([key_, DICT_RECORDS.get('VIR')])
        # for value in USLUGI.values():
        #     print(value)
        #     print(key)
            # if key == value:
                # print(DICT_RECORDS.get('VIR'))
                # LIST_test.append(DICT_RECORDS.get('VIR'))
                # print(float("{0:.2f}".format(DICT_RECORDS.get('VIR') * 1.20)))
# print(DICT_test)
# print(LIST_test)
# print(sum(LIST_test))
# print(sum(LIST_test) * 1.20)
    # LIST_test.append(DICT_RECORDS.get('KODUSL'))
    # LIST_DICT_ALL_KODUSL.append(DICT_RECORDS.get('KODUSL'))
    # LIST_DICT_ALL_OBEM.append(DICT_RECORDS.get('OBEM'))
    # LIST_DICT_ALL_VIR.append(DICT_RECORDS.get('VIR'))
# print(LIST_test)
# print(sum(LIST_test))
# print(sum(LIST_test) * 1.20)


def write_file_test():
    SUM_SET_DICT_ALL_KODUSL = set(LIST_DICT_ALL_KODUSL)
    SUM_LIST_DICT_ALL_KODUSL = []
    print(SUM_SET_DICT_ALL_KODUSL)
    for value in SUM_SET_DICT_ALL_KODUSL:
        value = value.replace(value, USLUGI.get(value))
        print(value)
        SUM_LIST_DICT_ALL_KODUSL.append(value)
    print(SUM_LIST_DICT_ALL_KODUSL)
    SUM_LIST_DICT_ALL_OBEM = sum(LIST_DICT_ALL_OBEM)
    print(SUM_LIST_DICT_ALL_OBEM)
    SUM_LIST_DICT_ALL_VIR = sum(LIST_DICT_ALL_VIR)
    print(SUM_LIST_DICT_ALL_VIR)

    with open('test.txt', 'w') as file:
        file.write(str(SUM_LIST_DICT_ALL_KODUSL))
        file.write('\n')
        file.write(str(SUM_LIST_DICT_ALL_OBEM))
        file.write('\n')
        file.write(str(SUM_LIST_DICT_ALL_VIR))


#write_file_test()
# print(dbfs_append())
# dbf_file = os.path.join('..', 'dbfs', '63053_10.dbf')
# print(dbf_file)
# table = dbfread.DBF(dbf_file, encoding='cp866')
# print(table)
#
# test_tuple1 = (
#     ('Ульяновский участок пересчета', 1111111, 1111111, 11111),
#     ('Пересчет', 11111111, 11111111, 11111),
#     ('Пересчет2', 2222222, 22222222, 22222222),
#               )
#
# test_tuple2 = (
#     ('Ульяновский участок инкассации', 3333333, 333333333, 8883333333888),
#     ('dssdsd', 777777, 888888, 888888),
#     ('dsdd', 2222222, 333333, 444444),
#     ('sdsd', 666666666, 333333, 444444),
#     ('dsdsd', 2222222, 333333, 444444),
#               )
#
# test_tuple3 = (
#     ('Димитровградский участок инкассации', 777777, 888888, 888888),
#     ('ffdfdf', 777777, 888888, 888888),
#     ('vcvccvcv', 2222222, 333333, 444444),
#     ('cscscscscs', 2222222, 333333, 444444),
#               )
#
# sum_tuple = ('Итого', 23232323, 32323232, 2323232323)
#
# tuple_ = (test_tuple1, test_tuple2, test_tuple3)



