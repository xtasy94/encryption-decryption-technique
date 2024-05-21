import random
import string

def generate_random_string(length):
    """Generate a random string of fixed length."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def convert_constant_to_numbers(constant):
    """Convert an alphanumeric constant to a list of numbers."""
    numbers = []
    for char in constant:
        if char.isdigit():
            numbers.append(int(char))
        elif char.isalpha():
            # Reverse alphabetical order: a=26, b=25, ..., z=1
            numbers.append(27 - (ord(char.lower()) - ord('a') + 1))
    return numbers

def encrypt_message(constant, plaintext):
    numeric_constant = convert_constant_to_numbers(constant)
    encrypted_message = []
    for i, char in enumerate(plaintext):
        shift = numeric_constant[i % len(numeric_constant)]
        random_string = generate_random_string(shift)
        encrypted_message.append(random_string + char)
    return ''.join(encrypted_message)

# Input
constant = input("Enter the alphanumeric constant: ")
plaintext = input("Enter the plaintext message: ")

# Encryption
encrypted_message = encrypt_message(constant, plaintext)
print("Encrypted Message:", encrypted_message)
