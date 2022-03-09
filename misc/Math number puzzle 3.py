"""
    STCD
  - CDTS
  -------
    TTDT
S for Square, T for Triangle, C for Circle, and D for Diamond.
"""
import re, itertools
def solve(puzzle):
    words = re.findall('[CDST]+', puzzle.upper())
    unique_characters = set(''.join(words))
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
            if eval(equation) and equation[0]=='7':
                return equation
    return "Not Found!"   

solve("STCD - CDTS == TTDT")
# '7340 - 4037 == 3303'


