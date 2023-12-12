import json
import base64
import datetime


class Person:
    def __init__(self, nomer, fam, name, otch, n_zachet,
                 fac2, vid_edu, kurs, d_prikaz_include,
                 date_end, n_specializ, photo, digit_sign):
        self.nomer = nomer
        self.fam = fam
        self.name = name
        self.otch = otch
        self.n_zachet = n_zachet
        self.fac2 = fac2
        self.vid_edu = vid_edu
        self.kurs = kurs
        self.d_prikaz_include = d_prikaz_include
        self.date_end = date_end
        self.n_specializ = n_specializ
        self.photo = photo
        self.digit_sign = digit_sign

    def __str__(self):
        return f'''
        Person(
        nomer={self.nomer},
        fam={self.fam},
        name={self.name},
        otch={self.otch},
        n_zachet={self.n_zachet},
        fac2={self.fac2},
        vid_edu={self.vid_edu},
        kurs={self.kurs},
        d_prikaz_include={self.d_prikaz_include},
        date_end={self.date_end},
        n_specializ={self.n_specializ},
        photo={self.photo},
        digit_sign={self.digit_sign}
        )
        '''

    def __json__(self):
        photo = ''
        if self.photo:
            photo = base64.b64encode(self.photo).decode('utf-8')

        digit_sign = ''
        if self.digit_sign:
            digit_sign = base64.b64encode(self.digit_sign).decode('utf-8')
        return {
            "nomer": self.nomer,
            "fam": self.fam,
            "name": self.name,
            "otch": self.otch,
            "n_zachet": self.n_zachet,
            "fac2": self.fac2,
            "vid_edu": self.vid_edu,
            "kurs": self.kurs,
            "d_prikaz_include": datetime.datetime.strptime(self.d_prikaz_include, "%Y-%m-%d %H:%M:%S").date(),
            "date_end": datetime.datetime.strptime(self.date_end, "%Y-%m-%d %H:%M:%S").date(),
            "n_specializ": self.n_specializ,
            "photo": json.dumps(photo),
            "digit_sign": json.dumps(digit_sign)
        }

    def get_fio(self):
        return f"{self.fam} {self.name} {self.otch}"
