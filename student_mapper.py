import io

import PIL.Image
import sys

sys.path.append("C:\\Users\\kulevets_v\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\fdb")
import fdb.fbcore
from PIL import UnidentifiedImageError

import Student as st


def unpack_sql_query_results_into_student_entities(sql_query_results):
    students = []
    for row in sql_query_results:
        student = st.Person(
            nomer=row[0],
            fam=row[1],
            name=row[2],
            otch=row[3],
            n_zachet=row[4],
            fac2=row[5],
            vid_edu=row[6],
            kurs=row[7],
            d_prikaz_include=str(row[8]),
            date_end=str(row[9]),
            n_specializ=row[10],
            photo=row[11],
            digit_sign=row[12]
        )
        # set_student_photo(student)
        save_student_photo(student)
        save_student_sign(student)
        students.append(student)
    return students


def set_student_photo(person):
    try:
        path = 'C:\\Users\\kulevets_v\\za4etcker-project\\za4etker\\src\\main\\resources\\student_photo\\'
        photo_path = person.get_fio() + '.JPG'
        photo = PIL.Image.open(f"{path}{photo_path}",
                               formats=["JPEG"])
        # photo_bytes = photo.tobytes("hex", "rgb")
        person.photo = f"{path}{photo_path}"
    except UnidentifiedImageError:
        person.photo = None
    except FileNotFoundError:
        person.photo = None


def save_student_photo(student):
    try:
        photo_bytes = None
        if isinstance(student.photo, fdb.BlobReader):
            photo_bytes = student.photo.read()
        elif isinstance(student.photo, bytes):
            photo_bytes = student.photo
        path = 'C:\\Users\\kulevets_v\\za4etcker-project\\za4etker\\src\\main\\resources\\student_photo\\'
        photo_name = student.get_fio()
        im = PIL.Image.open(io.BytesIO(photo_bytes))
        im.save(f"{path}{photo_name}.JPG")
        student.photo = f"{path}{student.get_fio()}.JPG"
    except UnidentifiedImageError:
        student.photo = None
    except FileNotFoundError:
        student.photo = None


def save_student_sign(student):
    try:
        sign_bytes = None
        if isinstance(student.digit_sign, fdb.BlobReader):
            sign_bytes = student.digit_sign.read()
        elif isinstance(student.digit_sign, bytes):
            sign_bytes = student.digit_sign
        path = 'C:\\Users\\kulevets_v\\za4etcker-project\\za4etker\\src\\main\\resources\\signs\\'
        sign_name = student.get_fio()
        im = PIL.Image.open(io.BytesIO(sign_bytes))
        im.save(f"{path}{sign_name}.JPG")
        student.digit_sign = f"{path}{student.get_fio()}.JPG"
    except UnidentifiedImageError:
        student.digit_sign = None
    except FileNotFoundError:
        student.digit_sign = None
