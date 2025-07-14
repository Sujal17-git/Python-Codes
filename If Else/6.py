# Take input of three sides
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

# Check if it forms a valid triangle
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("It's an Equilateral Triangle 🔺 (All sides equal)")
    else:
        if a == b or b == c or a == c:
            print("It's an Isosceles Triangle 📐 (Two sides equal)")
        else:
            print("It's a Scalene Triangle 🧷 (All sides different)")
else:
    print("Not a valid triangle ❌")
