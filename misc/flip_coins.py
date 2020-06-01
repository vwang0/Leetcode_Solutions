
# Expected number of coin flips to get head, tail in a row
# Expected number of coin flips to get two/three heads consecutively 

import numpy as np

def flip_coin(p=0.5):
    """
    Simulate flipping a coin.
    Parameters
    -------
    p : Parameter of the distribution, >= 0 and <=1.
    
    Returns
    -------
    str: "H" for heads/ "T" for tails.
    """
    
    flip = np.random.binomial(1, p, 1)
    if flip == 0:
        side = "T"
    else:
        side = "H"
    return side

def flip_pattern(end_pattern=['H', 'T'], print_opt=False):
    """Flip coin until flip pattern is met.
    
    Parameters
    ----------
    pattern: list
        The sequence of flips to be matched before flipping stops.
    
    print_opt: bool
        Option to print the sequence of flips.
        
    Returns
    -------
    int
        The number of flips it took to match the pattern.
    """
    flip_list = []
    
    current_index = 0
    current_condition = None
    while current_condition != end_pattern:
        flip_list.append(flip_coin())
        if len(flip_list) >= len(end_pattern):
            current_condition = flip_list[-len(end_pattern):]            
            # current_condition = [flip_list[i] for i in range(current_index - len(end_pattern) +1 , current_index + 1)]
        else:
            pass
        current_index +=1
        
    if print_opt:
        print(flip_list)
    return current_index 

np.mean([flip_pattern(['H', 'T']) for i in range(10000)])

np.mean([flip_pattern(['H', 'H']) for i in range(10000)])

np.mean([flip_pattern(['H', 'H', 'H']) for i in range(10000)])