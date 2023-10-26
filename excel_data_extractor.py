import pandas as pd

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