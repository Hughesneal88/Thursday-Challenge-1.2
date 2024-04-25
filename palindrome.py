def is_palindrome(s):
    # Remove spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Ask the user to enter a string
user_input = input("Enter a string to check if it's a palindrome: ")

# Check if the entered string is a palindrome and print the result
print(is_palindrome(user_input))
