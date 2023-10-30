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
        return {
            "nomer": self.nomer,
            "fam": self.fam,
            "name": self.name,
            "otch": self.otch,
            "n_zachet": self.n_zachet,
            "fac2": self.fac2,
            "vid_edu": self.vid_edu,
            "kurs": self.kurs,
            "d_prikaz_include": self.d_prikaz_include,
            "date_end": self.date_end,
            "n_specializ": self.n_specializ,
            "photo": self.photo,
            "digit_sign": self.digit_sign,
        }

    def get_fio(self):
        return f"{self.fam} {self.name} {self.otch}"