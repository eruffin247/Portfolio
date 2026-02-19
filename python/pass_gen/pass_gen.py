# This is a program to generate a random password.

import random

characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-="
password = ""
for x in range(10):
    password += random.choice(characters)

print(f"Your new password is: {password}")