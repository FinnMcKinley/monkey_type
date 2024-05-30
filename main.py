""" Writes whatever file is inputed, using monkeys of course!
    Author: Finn McKinley
    Date: 30/05/2024
"""
import random as rdm
import time

START = time.time()

def read_file(filename):
    """ Reads a file given from filename and returns file content """
    file = open(filename)
    content = file.read()
    file.close()
    return content

def character_map(content):
    """ Takes every line from file and returns character map """
    characters = []
    for character in content:
        if character not in characters:
            characters.append(character)
    return characters

def random_letter(character_map):
    """ Selects a random letter from the character map """
    return character_map[rdm.randint(0, len(character_map) -1)]

def file_guesser(filename):
    """ Randomly guesses its way through a file """
    content = read_file(filename)
    CHARACTERS = character_map(content)
    solution = ''
    for character in content:
        guess = random_letter(CHARACTERS)
        while guess != character:
            guess = random_letter(CHARACTERS)
        solution += character
    return solution

def get_filename():
    """ Asks the user for the filename until it exists """
    prompt = 'What is the filename you want to run? '
    generic_error = 'Sorry that is not a valid filename!'
    
    is_valid = False
    while is_valid == False:
        user_in = input(prompt)
        try: 
            file = open(user_in)
        except:
            print(generic_error)
        else:
            print('')
            is_valid = True
    return user_in

def main():
    """ Runs all of the code together
    """
    filename = get_filename()
    print(file_guesser(filename))

            
main()

# Tracks Program Runtime
END = time.time()
print(f'\n** The time of execution of above program is : {(END - START) * 10**3} ms **')
