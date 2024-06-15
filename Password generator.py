import random
import string as str
ascii = str.ascii_letters
digits = str.digits
symbols = str.punctuation
def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += ascii
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols
    if not (use_letters or use_digits or use_symbols):
        print("Error: At least one character set must be selected.")
        return None
    merge = random.sample(characters, length)
    generated_password = ''.join(merge)
    return generated_password
def main():
    print("Welcome to our random password generator")
    length = int(input("Enter the length of your password: "))
    use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_letters, use_digits, use_symbols)
    if password:
        print("Your generated password is:", password)

if __name__ == "__main__":
    main()