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
n_zachet_column = 'N_ZACHET'
excel_file = pd.ExcelFile('C:\\Users\\TSO\\Downloads\\1\\МВС\\!печать\\З\\МВС 2023.xlsx')
sheet_names = ['Дневное', 'Заочное']
sheet_data = []
for sheet_name in sheet_names:
    sheet_data.append(excel_file.parse(sheet_name))

n_zachet_data = {}
for index1, data in enumerate(sheet_data):
    for index, data_element in enumerate(data[n_zachet_column]):
        if index != len(data) - 1:
            data_element = "\'" + str(data_element) + "\',"
        else:
            data_element = "\'" + str(data_element) + "\'"
        print(data_element)
    n_zachet_data[(sheet_names[1], sheet_names[0])[index1 == 0]] = data[n_zachet_column]
print(n_zachet_data)
# cur = con.cursor()
# cur.execute(f"select * from people where n_zachet in()")
# print(cur.fetchall())
# cur.close()
