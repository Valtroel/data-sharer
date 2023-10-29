import fdb
import pandas as pd
import xlsxwriter

from Student import Student

# python -m pip install XlsxWriter

# connect to fb
# con = fdb.connect(
#     dsn="172.16.1.30/3050:dekanat",
#     user="sysdba",
#     password="dbudfV544703",
#     charset="UTF8"
# )

# cur = con.cursor()
# cur.execute(f"select * from people where n_zachet in()")
# print(cur.fetchall())
# cur.close()
