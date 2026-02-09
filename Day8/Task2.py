class Student:
    # Class Variable
    college_name = "ABC College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)

    # Class Method
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    # Static Method
    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"


student1 = Student("Dhanush", 101)
student2 = Student("Arjun", 102)

student1.display()
student2.display()

print("------------------")

# Change college name
Student.change_college("XYZ University")

student1.display()
student2.display()

print("------------------")

# Static method check
print(Student.is_pass(78))
print(Student.is_pass(30))
