class Student:
    collage_name = "GLS University"

    def __init__(self):
        print("New Student Created:")

    def hello(self,name):
        print("Welcome",name)

    def get_marks(self,marks):
        print("Your Marks is ",marks)

student1 = Student()
student1.hello("Sujal")
student1.get_marks(85)
print(student1.collage_name)