class Person():
    """docstring for Person"""
    def __init__(self, name,family):
        self.name = name
        self.family = family

    def showInfo(self):
        print(f'information --> {self.name} {self.family}')

class Student(Person):
    """docstring for Student"""
    __registerList = []
    def __init__(self,name,family,score):
        # Person.__init__(self,name,family)
        super().__init__(name,family)
        self.score = score

    def register(self):
        Student.__registerList.append(self.name)
        print(f'{self.name} Registered!!')

    def showRegister():
        print(Student.__registerList)

student1 = Student('Mohammad','Hassanpour',34)
student1.showInfo()
student1.register()
Student.showRegister()

student2 = Student('Hosein','Hassanpour',100)
student2.showInfo()
student2.register()
Student.showRegister()

