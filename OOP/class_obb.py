class Student:
     name = "Iron man"
     def __init__(self,name, marks):
          print("Adding New Student")
          self.name = name
          self.marks = marks
     

s1= Student("Raju",70)
print(s1.name,s1.marks)

s2 = Student("Tony",55)
print(s2.name,s2.marks)

s3 = Student()
print(s3.name)
