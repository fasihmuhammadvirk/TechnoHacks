#random password generator?
import string
import random

def generate_password(length):
    """
    Generates a random password of the given length.

    Parameters:
        length (int): The length of the password to be generated.

    Returns:
        str: The randomly generated password.
    """

    # The password will be composed of printable ascii characters
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the given length
    password = ''.join(random.choice(chars) for i in range(length))
    return password


length = int(input("Enter the Length of Your Password: "))
password = generate_password(length)
print("Generated password:", password)