import random

choices = ('rock','paper','scissor')

while True:

    user_choice =input("Rock / Paper / Scissor :").lower()

    if user_choice not in choices:
        print("Invalid Choice!")
    else:

        computer_choice = random.choice(choices)
        print(f"User choice : {user_choice}")
        print(f"Computer Choice : {computer_choice}")

        if user_choice == computer_choice:
            print("Match Draw")
        elif((user_choice=='rock' and computer_choice=='paper')or
            (user_choice=='paper' and computer_choice=='scissor')or
            (user_choice=='scissor' and computer_choice=='rock')):
            print("You Lose")
        else:
            print("You Won")
        
        should_again = input("Write 'Exit' to Leave Game or press any key to continue :").lower()

        if(should_again=='exit'):
            print("\n Bye Bye")
            break
    