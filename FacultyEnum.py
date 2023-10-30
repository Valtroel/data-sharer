from enum import Enum


class Faculty(Enum):
    MVS = "МВС"
    MSTIG = "МСТиГ"
    OFK = "ОФК"
    CIIE = "СИиЕ"


def get_faculty_from_path(path):
    for faculty in Faculty:
        if faculty.value in path:
            return faculty.value
    return "undefined"
