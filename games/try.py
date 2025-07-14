import random

choices =('rock','paper','scissor')

while True:

    user_choice = input("Rock/Paper/Scissor :")

    if user_choice not in choices:
        print("Please Enter Valid Choice!")

    else:

        computer_choice = random.choice(choices)
        print(f"\nUser Choice- {user_choice}")
        print(f"Computer Choice- {computer_choice}")

        if ((user_choice == 'rock' and computer_choice=='paper')or
            (user_choice=='paper' and computer_choice=='scissor')or
            (user_choice=='scissor' and computer_choice=='rock')):
            print("\n You Lose 👎")
        elif user_choice==computer_choice:
            print("\n Match Tie 🤝")
        else:
            print("\n 🏆 You Win 👑")

        wanna_exit = input("\n Press 'e' to EXIT The Game :")

        if wanna_exit =='e':
            break

