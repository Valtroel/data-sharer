import os
from pathlib import Path

directories_to_search = ['C:/Users/wwwlo/PycharmProjects/data-sharer/data/1']

def search_for_excel_files_paths():
    xlsx_files = []
    for directory in directories_to_search:
        dir_path = Path(directory).resolve()
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.xlsx'):
                    xlsx_files.append(os.path.join(root, file))
    return xlsx_files

