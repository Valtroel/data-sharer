import PIL.Image
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
            d_prikaz_include=row[8],
            date_end=row[9],
            n_specializ=row[10],
            photo=None,
            digit_sign=row[11]
        )
        set_student_photo(student)
        students.append(student)
    return students


def set_student_photo(person):
    try:
        photo_path = person.get_fio() + '.JPG'
        photo = PIL.Image.open(f"C:\\Users\\kulevets_v\\za4etcker\\data-sharer\\data\\photos\\{photo_path}")
        photo_bytes = photo.tobytes()
        person.photo = photo_bytes
    except UnidentifiedImageError:
        person.photo = None
    except FileNotFoundError:
        person.photo = None
