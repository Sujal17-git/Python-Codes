while True:

    choice = input("Enter you wanna print Square till numbers or Table (s/t) : ").lower()

    if choice=="s":
        Border = int(input("Enter Border number to get Square : "))
        for i in range(1,Border+1):
            print(f"{i} Square = {i*i}")
    elif choice=="t":
        Table = int(input("Enter which table you want : "))
        for i in range(1,11):
            print(f"{Table} X {i} = {Table*i}")
    
    repeat = input("wanna exit, press 'E': ").lower()

    if repeat=="e":
        break
