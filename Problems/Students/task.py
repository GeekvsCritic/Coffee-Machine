class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        print(f'{self.name[0]}{self.last_name}{self.birth_year}')


stu_id = Student(name=input(), last_name=input(), birth_year=input())
