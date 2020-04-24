'''
Monte Carlo Simulation: pi
N: total number of darts

random.random() gives you a random floating point number in the range [0.0, 1.0) 
(so including 0.0, but not including 1.0 which is also known as a semi-open range). 

random.uniform(a, b) gives you a random floating point number in the range [a, b], 
(where rounding may end up giving you b).

random.random()  generates a random float uniformly in the semi-open range [0.0, 1.0)
random.uniform() generates a random float uniformly in the range [0.0, 1.0].
'''

import random
def simu_pi(N):
    inside = 0
    for i in range(N):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if (x**2+y**2)<=1:
            inside +=1
    pi = 4*inside/N
    return pi

