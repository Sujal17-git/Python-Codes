def is_palindrome(s):
    # Base case: string of length 0 or 1 is a palindrome
    if len(s) <= 1:
        return True
    # If first and last characters don't match, it's not a palindrome
    if s[0] != s[-1]:
        return False
    # Recursive case: check the substring without first and last characters
    return is_palindrome(s[1:-1])

word = "NAMAN"
if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")
