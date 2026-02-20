# This is a program to generate a random password.

# This allows the random module to be used in this program. It is used to generate random numbers and make random choices.
# I switched to the secrets module because it is more secure than the random module for generating passwords. The secrets module is designed for generating cryptographically strong random numbers and is more suitable for generating passwords.
import secrets

# This is a string that contains all of the characters that can be used in the password.
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRZTUVWXYZ1234567890!@#$%^&*()_+-="

# This is an empty string that will be used to build the password, where it starts as empty and characters will be added to it in the loop below.
password = ""

# This is a loop that will run X amount of times, where X is the number of characters the password will have.
# The next line adds random characters X amount of times to the password string, where random.choice(characters) will randomly select a character from the characters string and add it to the password string.
for x in range(15):
    password += secrets.choice(characters)

print(f"Your new password is: {password}")