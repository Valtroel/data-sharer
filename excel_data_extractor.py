import pandas as pd
import excel_finder as ef
import logging as log

n_zachet_column = 'N_ZACHET'


def __get_excel_files():
    log.info("[__get_excel_files] Getting excel-files for parsing")
    excel_files = []
    for path in ef.search_for_excel_files_paths():
        excel_files.append(pd.ExcelFile(path))
    log.info(f"[__get_excel_files] Total parsed files: {len(excel_files)}")
    log.info(f"[__get_excel_files] End of files parsing")
    return excel_files


def __extract_sheets_data():
    log.info("[__extract_sheets_data] Start extracting sheets' data")
    sheets_data = {}
    excel_files = __get_excel_files()
    for excel_file in excel_files:
        log.info(f"[__extract_sheets_data] Process the next file: {excel_file.book}")
        for sheet_name in excel_file.sheet_names:
            log.info(f"[__extract_sheets_data] Process the next sheet {sheet_name} of {excel_file.book} file")
            data = excel_file.parse(sheet_name)
            sheets_data[sheet_name] = data[n_zachet_column].tolist()
            log.info(f"[__extract_sheets_data] Extracted from {sheet_name} sheet data: {sheets_data[sheet_name]}")
    return sheets_data


def get_n_zachet_data():
    log.info("[get_n_zachet_data] Start getting n_zachet column data from excel-files")
    n_zachet_data = {}
    sheets_data = __extract_sheets_data()
    for key, row_elements in sheets_data:
        for index, row in enumerate(row_elements[n_zachet_column]):
            if index != len(row_elements) - 1:
                row = "\'" + str(row) + "\',"
            else:
                row = "\'" + str(row) + "\'"
            print(row)
            n_zachet_data[key] = row_elements[n_zachet_column]
    return n_zachet_data


if __name__ == '__main__':
    print(get_n_zachet_data())
