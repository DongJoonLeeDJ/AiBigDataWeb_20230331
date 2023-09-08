class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"name={self.name}, age={self.age}")

a = Student("이동준",34)
b = Student(age=20,name="이유나")
a.introduce()
b.introduce()
print(a) # <__main__.Student object at 0x00000298F3E20E50>