import string
import random

def generate_password(length, include_numbers=True, include_specials=True, include_uppercase=True):
    upper = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_numbers else ''
    specials = '@_#$^' if include_specials else ''
    lower = string.ascii_lowercase 

    password_char = []

    if include_numbers:
        password_char.append(random.choice(digits))
    if include_specials:
        password_char.append(random.choice(specials))
    if include_uppercase:
        password_char.append(random.choice(upper))

    every_characters = upper + digits + lower + specials
    while len(password_char) < length:
        password_char.append(random.choice(every_characters))

    random.shuffle(password_char)
    password = ''.join(password_char)   

    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Enter a positive number")
            else:
                break
        except ValueError:
            print("Enter a valid number")

    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_specials = input("Include special characters? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    min_length = int(include_numbers) + int(include_specials) + int(include_uppercase)
    if length < min_length:
        print(f"The length of the password must be at least {min_length} with all types included.")
        return
    
    password = generate_password(length, include_numbers, include_specials, include_uppercase)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
 