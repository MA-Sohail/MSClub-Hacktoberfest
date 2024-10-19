import re

def is_palindrome(s: str) -> bool:
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    
    # Compare characters from the start and end moving towards the center
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    word = input("Enter a word or phrase: ")
    print(f'"{word}" is a palindrome: {is_palindrome(word)}')
