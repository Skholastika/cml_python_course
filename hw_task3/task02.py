class StudyMaterials:
    names = []

    def __init__(self, *args: str):
        self.names.extend(args)


class Student:
    students = []

    def __init__(self):
        if type(self) is Student:
            self.knowledge = []
            Student.students.append(self)

    def take(self, material_name: str):
        if material_name not in self.knowledge:
            self.knowledge.append(material_name)


class Teacher(Student):
    def __init__(self):
        super().__init__()
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
teacher1 = Teacher()
stud1 = Student()
stud2 = Student()
stud3 = Student()
stud4 = Student()

teacher1.teach(studies.names[0], 3)
teacher1.teach(studies.names[3], 1)
teacher1.teach(studies.names[0], 1)
teacher1.teach(studies.names[4], 4)
teacher1.teach(studies.names[1], 1)

print(teacher1.stud_num)
print(stud1.knowledge, stud2.knowledge, stud3.knowledge, stud4.knowledge)

