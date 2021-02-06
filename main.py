# Create a random password from criteria that the user inputs
# Criteria:
# - how many characters the password should be (can be a range e.g. between 10 and 15 characters long)
# - what type of characters to include (alphabetical, numeric, symbols) 
# - include a certain phrase in the password that the user inputs (e.g. stefan, mald0n, england27, etc.)

# Extra challenges:
# - include an extra feature that tests the user's current password's strength (e.g. weak, medium, strong)
# - create a GUI for the program

from classes import Prompter, Generator









    




def main():
    prompter = Prompter()
    generator = Generator()
    
    
    run = prompter.user_choice(prompter.initial_prompt, "G", "S")
    while run:
        generator.password_choices()
        run = generator.user_choice(generator.try_again, "G", "Q")


if __name__ == '__main__':
    main()
