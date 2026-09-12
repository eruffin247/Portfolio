# Functions for password generation.
import secrets

def gen_password(pass_length):
    temp_password = ""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+"
    for i in range(pass_length):
        temp_password += secrets.choice(characters)
    return temp_password