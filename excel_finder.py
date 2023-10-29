import os
import logging as log
from pathlib import Path

directories_to_search = ['C:\\Users\\wwlo\\zachetker\\data-sharer\\data\\1']


def search_for_excel_files_paths():
    log.info(f"[search_for_excel_files_paths] Starting of searching for excel-files path in {directories_to_search}")
    xlsx_file_names = []
    for directory in directories_to_search:
        dir_path = Path(directory).resolve()
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.xlsx') or file.endswith('.xls'):
                    found_path = os.path.join(root, file)
                    log.info(f"[search_for_excel_files_paths] Found path: {found_path}")
                    xlsx_file_names.append(found_path)
    log.info(f"[search_for_excel_files_paths] Ending of searching")
    return xlsx_file_names



if __name__ == '__main__':
    print(search_for_excel_files_paths())