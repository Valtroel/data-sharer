import fdb
import pandas as pd
import excel_data_extractor as ede

con = fdb.connect(
    dsn="172.16.1.30/3050:dekanat",
    user="sysdba",
    password="dbudfV544703",
    charset="UTF8"
)

excel_n_zachet_data = ede.get_n_zachet_data()
sql_stud = ("select people.nomer, people.fam, people.name, people.otch, people.n_zachet,\
                faculty.fac2, vid_edu.vid_edu, people.kurs, people.d_prikaz_include, \
                people.date_end, people.n_specializ, people.photo, people.digit_sign \
             from people, faculty, vid_edu, specializ  \
             where people.status_people = 1  \
                and faculty.n_fac = people.n_fac \
                and vid_edu.id_vid_edu = people.vid_edu \
                and people.n_specializ = specializ.n_specializ \
                and (people.n_zachet containing :nom_z or people.fam containing :fam) \
             order by people.n_zachet")

sql_mag = ("select student_tr.nomer, student_tr.fam, student_tr.name, student_tr.otch, student_tr.n_zachet, \
                faculty.fac2, vid_edu.vid_edu, student_tr.kurs, student_tr.d_prikaz_include,  \
                student_tr.date_end, specializ.special_direction, student_tr.photo, student_tr.digit_sign  \
            from student_tr, faculty, vid_edu, specializ \
            where faculty.n_fac = student_tr.id_fac \
                and vid_edu.id_vid_edu = student_tr.id_vid_edu \
                and student_tr.id_spec = specializ.n_specializ \
                and (student_tr.n_zachet containing :nom_z or student_tr.fam containing :fam) \
            order by student_tr.n_zachet")

cur = con.cursor()
cur.execute(f"select * from p where n_zachet in()")
print(cur.fetchall())
cur.close()
