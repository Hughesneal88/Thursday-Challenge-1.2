# Thursday-Challenge-1.2



# Palindrome Checker

A Python function to check if a given text is a palindrome.

## Function

```python
def is_palindrome(text):
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]
```
## How it works
- Takes input
- Removes whitespace
- Checks if cleaned text is same as its reverse
- Returns True if palindrome, False otherwise

## Usage


print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False

- Works with strings, numbers, symbols
- Case-insensitive
- Ignores whitespace

## Explanation

A simple and concise solution using built-in string methods and slicing.