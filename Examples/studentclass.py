class Student:
    department = 'Computer Science'
    count=0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Student.count=Student.count+1
        self.email = f'{self.name}@metropolia.fi'
    def __str__(self):
        return f'{self.name} {self.age} {self.gender}'
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_gender(self, gender):
        self.gender = gender

student_1 = Student("Alex", 20, "Male")
student_2 = Student("Bob", 30, "Female")
print(str(student_1), Student.department)
print(f"number of students is: {Student.count}")