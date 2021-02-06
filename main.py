# Create a random password from criteria that the user inputs
# Criteria:
# - how many characters the password should be (can be a range e.g. between 10 and 15 characters long)
# - what type of characters to include (alphabetical, numeric, symbols) 
# - include a certain phrase in the password that the user inputs (e.g. stefan, mald0n, england27, etc.)

# Extra challenges:
# - include an extra feature that tests the user's current password's strength (e.g. weak, medium, strong)
# - create a GUI for the program

import random
import string

alphabet = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
numbers = [str(i) for i in range(10)]
symbols = ['!', '@' , '#', '$', '%', '&', '*', '_', '-' , '?', '!', '@' , '#', '$', '%', '&', '*', '_', '-' , '?']

generate_or_quit = "Press (G) to generate a new random password or (Q) to quit: "
try_again = "Press (G) to try again or (Q) to quit: "
password_numbers = "Would you like your new password to contain numbers? (Y/N): "
password_uppers = "Would you like your new password to contain uppercase letters? (Y/N): "
password_symbols = "Would you like your new password to contain symbols? (Y/N): "


def user_choice(choices, a, b):
    user_input = None
    while user_input != a and user_input != b:
        user_input = input(choices).upper()
        if user_input == a:
            return True
        elif user_input == b:
            return False
        else:   
            print("Invalid user input")


def generate_password(password_characters, password_length):
    new_password = []

    while len(new_password) != password_length:
        new_password.append(random.choice(password_characters))

    print("This is your new password: {}".format(''.join(new_password)))
    

def password_choices():
    characters = alphabet

    if user_choice(password_numbers, "Y", "N"):
        characters += numbers
    if user_choice(password_uppers, "Y", "N"):
        characters += alphabet_upper
    if user_choice(password_symbols, "Y", "N"):
        characters += symbols
    password_length = int(input("Please state how many characters long you would like your new password to be: "))

    generate_password(characters, password_length)


def main():

    print("Welcome to Stef's Random Password Generator!!\n\n")
    run = user_choice(generate_or_quit, "G", "Q")
    while run:
        password_choices()
        run = user_choice(try_again, "G", "Q")


if __name__ == '__main__':
    main()
