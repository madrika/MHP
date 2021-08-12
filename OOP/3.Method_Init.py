class Student():
    """docstring for Student"""
    def __init__(self, name,family,grade,number):
        self.name = name
        self.family = family
        self.grade = grade
        self.number = number

    def showInfo(self):
        print(f'{self.name} {self.family} information -- > number: {self.number}, grade: {self.grade}')

Student1 = Student("Mohammad","Hassanpour",100,989115727018)
print(Student1.name)
Student1.showInfo()
Student2 = Student("Hosein","Hassanpour",200,989115727018)
print(Student2.name)
Student2.showInfo()