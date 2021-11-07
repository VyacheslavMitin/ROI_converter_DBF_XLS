import os
import sys
from read_dbfs import dbfs_append

print(dbfs_append())

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

#
# list_dict_records = []
# dict_records = {}
# for record in table:
#     dict_records.update(record)
#     list_dict_records.append(dict_records.get('VIR'))
# print(dict_records)
# print(list_dict_records)
# print(len(list_dict_records))
# print(sum(list_dict_records))


