import random
import string


alphabet = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
numbers = [str(i) for i in range(10)]
symbols = ['!', '@' , '#', '$', '%', '&', '*', '_', '-' , '?', '!', '@' , '#', '$', '%', '&', '*', '_', '-' , '?']




class Prompter:
  def __init__(self):
    self.initial_prompt = "Press (G) to use the Random Password Generator or (S) to use the Password Strength Tester: "
    print("Welcome to Stef's Random Password Generator!!\n\n")

  
  def user_choice(self, prompt, a, b):
    user_input = None
    while user_input != a and user_input != b:
        user_input = input(prompt).upper()
        if user_input == a:
            return True
        elif user_input == b:
            return False
        else:   
            print("Invalid user input")



class Generator(Prompter):
  def __init__(self):
    self.generate_or_quit = "Press (G) to generate a new random password or (Q) to quit: "
    self.try_again = "Press (G) to try again or (Q) to quit: "
    self.password_numbers = "Would you like your new password to contain numbers? (Y/N): "
    self.password_uppers = "Would you like your new password to contain uppercase letters? (Y/N): "
    self.password_symbols = "Would you like your new password to contain symbols? (Y/N): "


  def generate_password(self, password_characters, password_length):
    new_password = []

    while len(new_password) != password_length:
        new_password.append(random.choice(password_characters))

    print("This is your new password: {}".format(''.join(new_password)))


  def password_choices(self):
    characters = alphabet

    if self.user_choice(self.password_numbers, "Y", "N"):
        characters += numbers
    if self.user_choice(self.password_uppers, "Y", "N"):
        characters += alphabet_upper
    if self.user_choice(self.password_symbols, "Y", "N"):
        characters += symbols
    password_length = int(input("Please state how many characters long you would like your new password to be: "))

    self.generate_password(characters, password_length)





class Tester(Prompter):
  pass