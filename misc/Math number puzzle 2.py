"""
字母转数字通用解法
"""

import re, itertools
def solve(puzzle):
    ans = []
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, "It's bullshit!"
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
                ans.append(equation)
    return ans if ans else "Not Found!"    

solve("STCD - CDTS == TTDT")
# ['6329 - 2936 == 3393', '7340 - 4037 == 3303']

solve("WHITE + WATER == PICNIC")
# ['83642 + 85427 == 169069', '85642 + 83427 == 169069']


"""
    STCD
  - CDTS
  -------
    TTDT
S for Square, T for Triangle, C for Circle, and D for Diamond.

字母转数字通用解法

"""