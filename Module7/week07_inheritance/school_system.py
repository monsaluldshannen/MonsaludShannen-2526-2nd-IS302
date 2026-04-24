class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_info(self):
        super().display_info()
        print("Course:", self.course)

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print("Subject:", self.subject)

# Example Usage
student1 = Student("Alice", 19, "BSCS")
teacher1 = Teacher("Mr. Smith", 40, "Mathematics")

student1.display_info()
print()
teacher1.display_info()