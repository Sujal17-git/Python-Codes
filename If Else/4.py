
#GradingSystem

Maths = int(input("Enter Maths marks:"))
English = int(input("Enter English marks:"))
Science = int(input("Enter Science marks:"))

Percentage = (Maths+English+Science)/3

print(f"Percentage : {Percentage:.2f}")

if(Percentage>=90 and Percentage<100):
    print("Congratulations You Got 'A+'")
elif(Percentage>=80 and Percentage<90):
    print("Welldone You got 'A'")
elif(Percentage>=70 and Percentage<80):
    print("Nice You Got 'B'")
elif(Percentage>=60 and Percentage<70):
    print("Need Improvement You dot 'C'")
elif(Percentage>=50 and Percentage<60):
    print("You just Passed the Exam")
elif(Percentage<50):
    print("You Fail")
else:
    print("Please Enter Valid Percentage")
