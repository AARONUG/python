class StudentRegistration:
    def __init__(self, student_name, registration_number):
        self.student_name = student_name
        self.registration_number = registration_number

    def display_info(self):
        return f"Student Name: {self.student_name}, Registration Number: {self.registration_number}"

# MY REG NUMBER
if __name__ == "__main__":
    student1 = StudentRegistration("AARON KWESIGA", "S23/BBUC/BSIT/010")
    print(student1.display_info())


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

    def display(self):
        perimeter = self.Perimeter()
        area = self.Area()
        print(f"Length: {self.length}, Width: {self.width}, Perimeter: {perimeter}, Area: {area}")


class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def Volume(self):
        return self.Area() * self.height


# Example usage:
rectangle = Rectangle(30, 10)
rectangle.display()

parallelepiped = Parallelepiped(20, 15, 7)
print(f"Volume of Parallelepiped: {parallelepiped.Volume()}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print(f"Name: {self.name}, Age: {self.age}, Section: {self.section}")


# Example usage:
student = Student("AARON", "23", "BBUC")
student.displayStudent()



