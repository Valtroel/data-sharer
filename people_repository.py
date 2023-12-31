import math
import fdb
import excel_data_extractor as ede
import logging as log
import student_mapper as mapper

con = fdb.connect(
    dsn="172.16.1.30/3050:dekanat",
    user="sysdba",
    password="dbudfV544703",
    charset="UTF8"
)

log.basicConfig(
    encoding='utf8',
    level=log.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    handlers=[log.FileHandler('logs/logs.log')]
)

sql_spec_query = '''
        SELECT DISTINCT people.n_specializ
        FROM people;
'''


def __prepare_queries(excel_files_paths=None):
    excel_n_zachet_data = ede.get_n_zachet_data_from_excel_files(excel_files_paths)
    sql_stud_queries_with_faculties = {}

    for fac, fac_n_zachet_data in excel_n_zachet_data.items():
        fac_clear_data = list(filter(lambda value: not math.isnan(float(value)), fac_n_zachet_data))
        log.debug(f"[people_repository] Prepared {len(fac_clear_data)} n_zachet values of {fac} faculty")
        sql_stud_queries_with_faculties[fac] = f'''
        select people.nomer, people.fam, people.name, people.otch, people.n_zachet,
                    faculty.fac2, vid_edu.vid_edu, people.kurs, people.d_prikaz_include, 
                    people.date_end, people.n_specializ, people.photo, people.digit_sign 
                 from people, faculty, vid_edu, specializ  
                 where people.status_people = 1  
                    and faculty.n_fac = people.n_fac 
                    and vid_edu.id_vid_edu = people.vid_edu 
                    and people.n_specializ = specializ.n_specializ
                    and people.n_zachet in({str(fac_clear_data).strip("[]")}) 
                 order by people.n_zachet
                 '''
        log.debug(f"[people_repository] Prepared SQL query: \n {sql_stud_queries_with_faculties[fac]}")

    sql_mag = f'''
        select student_tr.nomer, student_tr.fam, student_tr.name, student_tr.otch, student_tr.n_zachet, \
                    faculty.fac2, vid_edu.vid_edu, student_tr.kurs, student_tr.d_prikaz_include,  \
                    student_tr.date_end, specializ.special_direction, student_tr.photo, student_tr.digit_sign  \
                from student_tr, faculty, vid_edu, specializ \
                where faculty.n_fac = student_tr.id_fac \
                    and vid_edu.id_vid_edu = student_tr.id_vid_edu \
                    and student_tr.id_spec = specializ.n_specializ \
                    and (student_tr.n_zachet containing :nom_z or student_tr.fam containing :fam) \
                    and people.n_zachet in()\
                order by student_tr.n_zachet
                '''
    return sql_stud_queries_with_faculties


def find_people_by_n_zachet_data(excel_files_paths=None):
    people_separated_with_fac = []
    cur = con.cursor()
    for query in __prepare_queries(excel_files_paths).values():
        log.debug(f"[people_repository] Starting execute SQL query: \n {query}")
        cur.execute(query)
        sql_query_results = cur.fetchall()
        people_separated_with_fac = (people_separated_with_fac
                                     + mapper.unpack_sql_query_results_into_student_entities(sql_query_results))
    cur.close()
    return people_separated_with_fac


def find_all_n_specializ():
    cur = con.cursor()
    cur.execute(sql_spec_query)
    n_specializ_values = cur.fetchall()
    cur.close()
    return n_specializ_values
