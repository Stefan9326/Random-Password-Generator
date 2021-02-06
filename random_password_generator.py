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


def generate_password(password_characters, password_length):
    new_password = []

    while len(new_password) != password_length:
        new_password.append(random.choice(password_characters))

    print("This is your new password: {}".format(''.join(new_password)))
    

def ask_user_input():
    characters = alphabet

    password_numbers = input("Would you like your new password to contain numbers? (Y/N): ").upper()
    password_uppers = input("Would you like your new password to contain uppercase letters? (Y/N): ").upper()
    password_symbols = input("Would you like your new password to contain symbols? (Y/N): ").upper()
    if password_numbers == "Y":
        characters += numbers
    if password_uppers == "Y":
        characters += alphabet_upper
    if password_symbols == "Y":
        characters += symbols
    password_length = int(input("Please state how many characters long you would like your new password to be: "))

    generate_password(characters, password_length)

def foo():
    user_input = None
    while user_input != "G" and user_input != "Q":
        user_input = input("Enter (G) to generate a new random password or (Q) to quit: ").upper()
        if user_input == "G":
            return True
        elif user_input == "Q":
            return False
        else:   
            print("Invalid user input")


def main():

    print("Welcome to Stef's Random Password Generator!!\n\n")
    run = foo()
   
    
    while run:
        ask_user_input()
        try_again = input("Press (G) to generate a different password or (Q) to quit: ").upper()
        if try_again == "Q":
            run = False


if __name__ == '__main__':
    main()
