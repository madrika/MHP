class Person:
    """This is Class For Person"""
    name = "Madrika"
    age = 41
    def func(self):
        print("This is a Method")

Person1 = Person()
print(Person1.age)
print(Person1.name)
Person1.func()
Person2 = Person()
print(Person2.age)
print(Person2.name)