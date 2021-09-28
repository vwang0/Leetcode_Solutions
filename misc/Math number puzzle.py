"""
Puzzles like below are called cryptarithms or alphametics. 
The letters spell out actual words, but if you replace each letter with a digit from 0–9, 
it also “spells” an arithmetic equation. The trick is to figure out which letter maps to each digit. 
All the occurrences of each letter must map to the same digit, 
no digit can be repeated, and no “word” can start with the digit 0.

This programsolves alphametic puzzles

HAWAII + IDAHO + IOWA + OHIO == STATES
510199 + 98153 + 9301 + 3593 == 621246
 
H = 5
A = 1
W = 0
I = 9
D = 8
O = 3
S = 6
T = 2
E = 4

"""
import re
import itertools
def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation
    return "Not Found!"    


    


solve("WHITE + WATER == PICNIC")
# '85642 + 83427 == 169069'

solve("HAWAII + IDAHO + IOWA + OHIO == STATES")
# '510199 + 98153 + 9301 + 3593 == 621246'

solve("SEND + MORE == MONEY")
# '9567 + 1085 == 10652'

solve("DAD + LOVE == EMILY")
# '464 + 9831 == 10295'

