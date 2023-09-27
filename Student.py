class Student:
    def __init__(self, id_student, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.id_student = id_student

    def get_gpa(self):
        return self.gpa

    def get_age(self):
        return self.age

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_major(self):
        return self.major

    def set_gpa(self, gpa):
        self.gpa = gpa

    def set_age(self, age):
        self.age = age

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_major(self, major):
        self.major = major

    def __str__(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\nMajor: " + self.major + "\nGPA: " + str(self.gpa)
