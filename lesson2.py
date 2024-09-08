class Student:
    count = 0
    def __init__(self, name, age=18, height=170):
        self.height = height
        self.name = name
        self.age = age
        Student.count += 1

    def show(self):
        print('=================')
        print("Ім'я = ", self.name)
        print("вік = ", self.age)
        print("зріст = ", self.height)
        print("count = ", self.count)

    def __str__(self):
        return "Hello, my name is " + self.name + "!"




jack_student = Student(name="Jack", age=15, height=160)
kirill_student = Student("Kirill", 14, 165)
bob_student = Student("Bob")
# print('=================')
# print("Ім'я = ", jack_student.name)
# print("вік = ", jack_student.age)
# print("зріст = ", jack_student.height)
# print("count = ", jack_student.count)
#
# print('=================')
# print("Ім'я = ", kirill_student.name)
# print("вік = ", kirill_student.age)
# print("зріст = ", kirill_student.height)
# print("count = ", kirill_student.count)
#
#
# print('=================')
# print("Ім'я = ", bob_student.name)
# print("вік = ", bob_student.age)
# print("зріст = ", bob_student.height)
# print("count = ", bob_student.count)
jack_student.show()
kirill_student.show()
bob_student.show()

print(jack_student)
print(kirill_student)
print(bob_student)