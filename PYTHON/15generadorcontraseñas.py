import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):

    chars = ""
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    
    
    if not chars:
        raise ValueError("At least one character type must be selected")
    
    # Generate the password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    
    length = int(input("Enter the password length: "))
    
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
