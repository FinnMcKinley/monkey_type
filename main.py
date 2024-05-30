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
    lines = file.read().splitlines()
    file.close()
    return lines

def character_map(lines):
    """ Takes every line from file and returns character map """
    characters = []
    for line in lines:
        for character in line:
            if character not in characters:
                characters.append(character)
    return characters

def random_letter(character_map):
    """ Selects a random letter from the character map """
    return character_map[rdm.randint(0, len(character_map) -1)]

def main():
    """ Runs all of the code together
    """
    lines = read_file('shakespeare.txt')
    CHARACTERS = character_map(lines)
    solution = ''
    for line in lines:
        for character in line:
            guess = random_letter(CHARACTERS)
            while guess != character:
                guess = random_letter(CHARACTERS)
            solution += character
    print(solution)
            
main()

# Tracks Program Runtime
END = time.time()
print(f'The time of execution of above program is : {(END - START) * 10**3}, ms')
