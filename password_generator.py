import secrets
import string

def generate_password(length, use_digits, use_symbols):
    chars = string.ascii_letters
    
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    return ''.join(secrets.choice(chars) for _ in range(length))

def main():
    try:
        length = int(input("Enter password length: "))
        
        digits_choice = input("Include numbers (y/n): ").lower() == 'y'
        symbols_choice = input("Include symbols (y/n): ").lower() == 'y'

        result = generate_password(length, digits_choice, symbols_choice)
        
        print("-" * 30)
        print(f"Generated Password: {result}")
        print("-" * 30)
        
    except ValueError:
        print("Error: Please enter a valid number for length.")

if __name__ == "__main__":
    main()