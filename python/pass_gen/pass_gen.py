# This is a program to generate a random password.

# This allows the random module to be used in this program. It is used to generate random numbers and make random choices.
import random

# This is a string that contains all of the characters that can be used in the password.
characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-="

# This is an empty string that will be used to build the password, where it starts as empty and characters will be added to it in the loop below.
password = ""

# This is a loop that will run X amount of times, where X is the number of characters the password will have.
# The next line adds random characters X amount of times to the password string, where random.choice(characters) will randomly select a character from the characters string and add it to the password string.
for x in range(10):
    password += random.choice(characters)

print(f"Your new password is: {password}")