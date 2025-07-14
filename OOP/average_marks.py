class Student:
    collage_name = "GLS University"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("Average of",self.name,"Marks is",sum/3)

s1 = Student("Sujal",[83,85,75])
print(s1.name,s1.marks)
s1.get_avg()

        