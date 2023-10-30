import os
import logging as log
from pathlib import Path
from datetime import datetime

directories_to_search = ['C:\\Users\\wwlo\\zachetker\\data-sharer\\data\\1']


def search_for_excel_files_paths():
    log.debug("[search_for_excel_files_paths] Начало поиска путей к файлам Excel")
    excel_files_paths = []
    for directory in directories_to_search:
        dir_path = Path(directory).resolve()
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.xlsx') or file.endswith('.xls'):
                    excel_files_paths.append(os.path.join(root, file))
    log.debug(f"[search_for_excel_files_paths] Найдено {len(excel_files_paths)} файлов Excel")
    log.debug("[search_for_excel_files_paths] Окончание поиска")
    return excel_files_paths

