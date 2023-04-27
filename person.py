import firstFile as ff


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age}'

    def greeting(self):
        print(f'Hello, {self.name}. Don\'t worry, {str(self.age)} isn\'t too much!')


me = Person('Dimarik', 34)
print(me.name, 'is', me.age, 'years old(')
print(me)
me.greeting()


class Student(Person):
    def __init__(self, name, age, graduate_year):
        super().__init__(name, age)
        self.graduate_year = graduate_year

    def greeting(self):
        print(f'Hello, {self.name}. {str(self.age)} is a nice age!. {self.graduate_year}')


student = Student('Dmytro', 17, 2011)
student.greeting()
print(ff.power_lambda(4, 2))
print(dir(ff))
