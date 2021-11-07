import os
import dbfread
from check_dbfs import checking_dbfs

DBF_TABLES = []


def dbfs_read(dbf_files: list):
    table = dbfread.DBF(dbf_files, encoding='cp866')
    return table


def dbfs_append() -> list:
    for tables in checking_dbfs():
        DBF_TABLES.append(dbfs_read(tables))
    return DBF_TABLES

