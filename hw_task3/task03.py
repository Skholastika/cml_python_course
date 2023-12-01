from random import randint


class Person:
    def __init__(self, name: str, surname: str, age: int, sex: str ):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex


class StudyMaterials:
    names = []

    def __init__(self, *args: str):
        self.names.extend(args)

    def __len__(self):
        return len(self.names)


class Student(Person):
    students = []

    def __init__(self, name: str, surname: str, age: int, sex: str):
        if type(self) is Student:
            self.knowledge = []
            Student.students.append(self)
            super().__init__(name, surname, age, sex)

    def __len__(self):
        return len(self.knowledge)

    def take(self, material_name: str):
        if material_name not in self.knowledge:
            self.knowledge.append(material_name)

    def forget(self):
        self.knowledge.pop(randint(0, len(self)-1))


class Teacher(Student):
    def __init__(self, name: str, surname: str, age: int, sex: str):
        super().__init__(name, surname, age, sex)
        self.stud_num = {}

    def teach(self, material_name: str, stud_num: int = 1):
        for student in Student.students[0:stud_num]:
            student.take(material_name)
            if self.stud_num.get(material_name):
                self.stud_num[material_name] = self.stud_num[material_name] + 1
            else:
                self.stud_num[material_name] = 1


studies = StudyMaterials("Python",
                         "Version Control Systems",
                         "Relational Databases",
                         "NoSQL databases",
                         "Message Brokers"
                         )

teacher1 = Teacher('Учитель', 'Учителев', 35, 'M')
stud1 = Student('Студентка', 'Первая', 12, "Ж")
stud2 = Student('Студентка', 'Вторая', 13, "Ж")
stud3 = Student('Студент', 'Третий', 12, "М")
stud4 = Student('Студент', 'Четвертый', 13, "М")

teacher1.teach(studies.names[0], 3)
teacher1.teach(studies.names[3], 1)
teacher1.teach(studies.names[0], 1)
teacher1.teach(studies.names[4], 4)
teacher1.teach(studies.names[1], 1)

print(teacher1.stud_num)
print(stud1.knowledge, stud2.knowledge, stud3.knowledge, stud4.knowledge)
stud1.forget()
del Student.students
print(stud1.knowledge)

