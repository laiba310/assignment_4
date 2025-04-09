import string
import random

# Function to check the strength of a given password
def check_password_strength(password):
    has_upper = any(char.isupper() for char in password)  # Check for uppercase letters
    has_lower = any(char.islower() for char in password)  # Check for lowercase letters
    has_digit = any(char.isdigit() for char in password)  # Check for digits
    has_symbols = any(char in string.punctuation for char in password)  # Check for special symbols

    missing = []  # List to track missing criteria

    # Check password length
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long.\n"

    # Check if any component is missing
    if not has_upper:
        missing.append("uppercase letters (A-Z)")
    if not has_lower:
        missing.append("lowercase letters (a-z)")
    if not has_digit:
        missing.append("digits (0-9)")
    if not has_symbols:
        missing.append("special symbols (!@#$%)")

    # If any components are missing, return the list of missing components
    if missing:
        return "Weak: Missing the following components:\n" + "\n".join(missing)
    
    return "Strong: Your password is strong!"

# Function to generate a random password of a given length
def generate_random_password(length=12):
    # Ensure the password is at least 8 characters long
    if length < 8:
        return "Weak password: Password length should be at least 8 characters."

    # Ensure the password contains at least one of each required component
    has_upper = random.choice(string.ascii_uppercase)
    has_lower = random.choice(string.ascii_lowercase)
    has_digit = random.choice(string.digits)
    has_symbols = random.choice(string.punctuation)

    # Combine all characters for the remaining part of the password
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = ''.join(random.choices(all_chars, k=length - 4))  # The remaining characters to fill the password

    # Create the password by combining the required components and the remaining characters
    password = list(has_upper + has_lower + has_digit + has_symbols + remaining_chars)

    # Shuffle the password to randomize the characters
    random.shuffle(password)

    # Join the characters and return the password
    return "".join(password)
generate_random_password()