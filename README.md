# Thursday-Challenge-1.2
# Palindrome Checker

This is a simple Python program to check if a given string is a palindrome.

## How it Works

The `is_palindrome` function takes a string as input, removes any spaces and converts it to lowercase. It then checks if the string is equal to its reverse (ignoring spaces and case). If the string is a palindrome, the function returns `True`; otherwise, it returns `False`.

## Usage

To use the palindrome checker:

1. Run the Python script.
2. Enter a string when prompted.
3. The program will output `True` if the entered string is a palindrome, and `False` otherwise.

## Example

```python
# Example usage of the is_palindrome function
user_input = input("Enter a string to check if it's a palindrome: ")
print(is_palindrome(user_input))
