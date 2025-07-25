"""PASSWORD GENERATOR

TASK 3

A password generator is a useful tool that generates strong and

random passwords for users. This project aims to create a
password generator application using Python, allowing users to

specify the length and complexity of the password.

User Input: Prompt the user to specify the desired length of the

password.

Generate Password: Use a combination of random characters to

generate a password of the specified length.

Display the Password: Print the generated password on the screen."""


import random
import string

# Ask user for the length of the password
length = int(input("Enter the desired password length: "))

# Combine all possible characters
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random password
password = ''.join(random.choice(characters) for _ in range(length))

# Show the generated password
print(f"Generated Password: {password}")


