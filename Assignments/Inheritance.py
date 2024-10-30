class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        return f"I am{self.name}, {self.age} years old, {self.gender}"

class Member(Person):
    def __init__(self, name, age, gender, membership_id):
        super().__init__(name, age, gender)
        self.membership_id = membership_id
    def introduce(self):
        return f"{super().introduce()} with membership ID: {self.membership}"

class Author(Person):
    def __init__(self, name, age, gender, books_written):
        super().__init__(name,age,gender)
        self.books_written = books_written
    def introduce(self):
        return f"Books written: {self.books_written}"

class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membership_id, books_written):
        Person.__init__(name, age, gender)
        self.membership_id = membership_id
        self.books_written = books_written
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender} with memberhip ID: {self.member}, Books written: {self.books_written}"

library_members= [
    AuthorMember("Mary", 20, "female", "M001", "abc"),
    AuthorMember("John", 21, "male", "M002", "cdb")
]
for member in library_members:
    print(member.introduce())
