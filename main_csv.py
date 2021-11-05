import csv
import dbfread


def dbf_to_table(dbf_file_path):
    table = (dbfread.DBF(f'{dbf_file_path}', encoding='cp866'))
    fields = table.field_names
    with open(f'{dbf_file_path[:-4]}.csv', 'w', newline='',
              encoding='utf-8-sig') as f:  # create a csv file, fill it with dbf content
        writer = csv.writer(f)
        writer.writerow(fields)  # write the column name
        for record in table:
            writer.writerow(list(record.values()))


dbf_to_table('63053_10.DBF')
