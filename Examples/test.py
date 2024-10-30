'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}"

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id
    def introduce(self):
       return f"I am {self.name}, {self.age} years old, {self.gender} and my student id is {self.student_id}"

class Assistant(Student):
    def __init__(self, name, age, gender, student_id, salary):
        super().__init__(name, age, gender, student_id)
        self.salary = salary
    def introduce(self):
        return f"My name is: {self.name}, and my student id is: {self.student_id}, My salary is {self.salary}"

student1 = Student("John", 30, "Male", 1234)
print(student1.introduce())
assistant1 = Assistant("Matti", "23", "M", 1234, "3773")
print(assistant1.introduce())


class Teacher(Person):
    def __init__(self, name, age, gender, teacher_title):
        super().__init__(name, age, gender)
        self.teacher_title = teacher_title
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}, my teacher title is {self.teacher_title}"

teachers=[]
teacher1 = Teacher("Matti", 23, "M", "Sr.Lecturer")
teacher2 = Teacher("Outi", 25, "f", "Lecturer")
teachers.append(teacher1)
teachers.append(teacher2)
for teacher in teachers:
    print(teacher.introduce())

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}"

class Teacher(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}"

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id
    def introduce(self):
       return f"I am {self.name}, {self.age} years old, {self.gender} and my student id is {self.student_id}"

class Assistant(Teacher):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender)
        self.salary = salary
    def introduce(self):
        return f"My name is: {self.name}, My salary is {self.salary}"

class PartTime(Teacher):
    def __init__(self, name, age, gender, hour):
        super().__init__(name, age, gender)
        self.hour = hour
    def introduce(self):
        return f"My name is: {self.name}, I am parttime teacher and my teaching hour is {self.hour}"

assistants=[]
assistant1 = Assistant("Matti", "23", "M", 1234)
assistants.append(assistant1)
assistant2 = Assistant("Outi", "25", "f", 2938)
assistants.append(assistant2)
for assistant in assistants:
    print(assistant.introduce())

parttimes=[]
parttime1 = PartTime("Matti", "23", "M", 1234)
parttime2 = PartTime("Outi", "25", "f", 2938)
parttimes.append(parttime1)
parttimes.append(parttime2)
for parttime in parttimes:
    print(parttime.introduce())
'''
class Person:
    counter=0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.counter+=1
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}"

class Teacher(Person):
    def __init__(self, teacher_title):
        self.teacher_title = teacher_title
    def introduce(self):
        return f"My teacher title is {self.teacher_title}"

class Student(Person, Teacher):
    def __init__(self, name, age, gender,teacher_title, student_id):
        Person.__init__(self, name, age, gender)
        Teacher.__init__(self, teacher_title)
        self.student_id = student_id