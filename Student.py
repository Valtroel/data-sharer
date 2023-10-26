class Student:
    def __init__(self, n_zachet, name, surname, father_name, faculty, speciality, date_end, photo, sign):
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.faculty = faculty
        self.speciality = speciality
        self.date_end = date_end
        self.photo = photo
        self.sign = sign
        self.n_zachet = n_zachet

    def __str__(self):
        return f'''
        Student:
            n_zachet: {self.n_zachet}
            name: {self.name}
            surname: {self.surname}
            father_name: {self.father_name}
            faculty: {self.faculty}
            speciality: {self.speciality}
            date_end: {self.date_end}
            photo: {self.photo}
            sign: {self.sign}
        '''

    def get_fio(self):
        return f"{self.surname} {self.name} {self.father_name}"
