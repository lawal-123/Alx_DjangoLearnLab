class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"student name: {self.name}")
        print(f"student age: {self.age}")
student1 = Student("allice", 30)
student1.display_info()
student2 = Student("diallo", 31)
student2.display_info()