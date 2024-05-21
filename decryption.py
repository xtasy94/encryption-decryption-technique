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

def decrypt_message(constant, encrypted_message):
    numeric_constant = convert_constant_to_numbers(constant)
    decrypted_message = []
    index = 0
    while index < len(encrypted_message):
        for shift in numeric_constant:
            if index >= len(encrypted_message):
                break
            index += shift
            if index < len(encrypted_message):
                decrypted_message.append(encrypted_message[index])
                index += 1
            else:
                break
    return ''.join(decrypted_message)

# Input
constant = input("Enter the alphanumeric constant: ")
encrypted_message = input("Enter the encrypted message: ")

# Decryption
decrypted_message = decrypt_message(constant, encrypted_message)
print("Decrypted Message:", decrypted_message)
