import random


while (True):

    choice = input("Enter your choice Y/N :").lower()
    if(choice=='y'):
         die1 = random.randint(1,6)
         die2 = random.randint(1,6)

         print(f"({die1},{die2})")

    elif choice=='n':
        print("Thankyou for playing this game")
        break

    else:
        print("Please enter valid input")