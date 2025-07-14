import random

number = random.randint(1,100)

while True:
    guess = int(input("Guess The Number :"))
    if number<guess:
        print("Too High")
    elif number>guess:
        print("Too Low")
    else:
        print("Gotch - You Hit the Bull's Eye ")
        break