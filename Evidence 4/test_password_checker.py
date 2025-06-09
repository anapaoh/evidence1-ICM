import re

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'

def check_password_strength(password):
    if re.match(pattern, password):
        return "STRONG"
    else:
        return "WEAK"

def main():
    try:
        with open('passwords.txt', 'r') as file:
            for line in file:
                password = line.strip()
                result = check_password_strength(password)
                print(f"{password}: {result}")
    except FileNotFoundError:
        print("Error: File 'passwords.txt' not found.")

if __name__ == "__main__":
    main()
