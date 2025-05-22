"""
This script checks password strength using regex and prints whether each password is strong or weak.
"""

import re

def is_strong(password):
    """Returns True if the password meets strength requirements."""
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    return re.match(pattern, password) is not None

def analyze_passwords(file_path):
    """Reads a file of passwords and prints if they are strong or weak."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        print("Password Strength Analysis:\n")
        for line in lines:
            pwd = line.strip()
            if is_strong(pwd):
                print(f"STRONG: {pwd}")
            else:
                print(f"Weak:   {pwd}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    analyze_passwords("password.txt")
