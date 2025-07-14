# Take input from user
char = input("Enter a single alphabet: ").lower()  # convert to lowercase

# Check if it's an alphabet
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(char, "is a Vowel ")
    else:
        print(char, "is a Consonant ")
else:
    print("Invalid input Please enter a single alphabet.")
