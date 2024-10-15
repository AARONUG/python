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
