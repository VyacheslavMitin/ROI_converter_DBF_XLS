import os
import dbfread
import check_dbfs


def dbf_read(dbf_files: list):
    table = dbfread.DBF(dbf_files, encoding='cp866')
    return table


DBF_TABLES = []
for files in check_dbfs.DBFS_FILES:
    DBF_TABLES.append(dbf_read(files))
print(DBF_TABLES)

os.chdir(os.path.join('..'))
print(os.getcwd())
