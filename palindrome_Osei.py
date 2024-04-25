def is_palindrome(text):
    # Convert the text to a string and remove whitespace while converting texts to lowercase
    cleaned_text = ''.join(text.lower().split())

    # Check if the cleaned text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]


# Prompt the user for input
user_input = input("Enter a text: ")

# Check if the input is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
