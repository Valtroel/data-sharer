import pandas as pd
import excel_finder as ef
import logging as log
import numpy as np
import FacultyEnum as fac
import ExcelFileData as ex_f

# Колонка из файла excel с нужными данными
n_zachet_column = 'N_ZACHET'


def __get_excel_files():
    log.debug("[__get_excel_files] Получение файлов Excel для обработки")
    excel_files = ef.search_for_excel_files_paths()
    log.debug(f"[__get_excel_files] Количество обработанных файлов: {len(excel_files)}")
    log.debug(f"[__get_excel_files] Окончание обработки файлов")
    return excel_files


def __extract_sheets_data():
    log.debug("[__extract_sheets_data] Start extracting sheets' data")
    sheets_data = {}
    excel_files = __get_excel_files()
    for excel_file_path in excel_files:
        file_key = fac.get_faculty_from_path(excel_file_path)
        excel_file = pd.ExcelFile(excel_file_path)
        log.debug(f"[__extract_sheets_data] Process the next file: {excel_file_path}")
        for sheet_name in excel_file.sheet_names:
            log.debug(f"[__extract_sheets_data] Process the next sheet {sheet_name} of {excel_file_path} file")
            data = excel_file.parse(sheet_name)
            n_zachet_values = data[n_zachet_column].tolist()
            if file_key in sheets_data:
                temp_data = sheets_data[file_key].data
                sheets_data.pop(file_key)
                sheets_data[file_key] = ex_f.ExcelFileData(path=excel_file_path, data=temp_data + n_zachet_values)
            else:
                sheets_data[file_key] = ex_f.ExcelFileData(path = excel_file_path, data = n_zachet_values)
            log.debug(f"[__extract_sheets_data] Extracted from {sheet_name} sheet data: {sheets_data[file_key]}")
    return sheets_data


def get_n_zachet_data_from_excel_files():
    elements_count = 0
    log.debug("[get_n_zachet_data] Начало получения данных из столбца `Номер зачета` из файлов Excel")
    n_zachet_excel_data = {}
    nan_values = {}
    sheets_data = __extract_sheets_data()
    for key, row_elements in sheets_data.items():
        row_data = row_elements
        for index, row in enumerate(row_data.data):
            if np.isnan(row):
                log.warning(f"[get_n_zachet_data_from_excel_files] Find nan value in the following path: \n "
                            f"{row_data.path}")
                continue
            elif index != len(row_elements.data) - 1:
                row = str(int(row))
                elements_count = elements_count + 1
            else:
                row = str(int(row))
                elements_count = elements_count + 1
            row_data.data[index] = row
            log.debug(f"[get_n_zachet_data][{key}] Обработан номер {row}")
            log.debug(f"[get_n_zachet_data] Обработано значений: {elements_count}")
        n_zachet_excel_data[key] = row_data.data
    return n_zachet_excel_data

