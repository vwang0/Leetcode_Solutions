"""
Find the smallest number N in a given range num that meet the criteria:
N, 2N, 3N, 4N, and 5N have the same digits.
"""

from collections import Counter
def findNum(N):
    for i in range(1,N):
        if Counter(str(i))== Counter(str(2*i)) 
        and Counter(str(2*i)) == Counter(str(3*i)) 
        and Counter(str(3*i)) == Counter(str(4*i)) 
        and Counter(str(4*i)) == Counter(str(5*i))
        and Counter(str(5*i)) == Counter(str(6*i)) :
            return i
    return print('Not Found!')


"""
N = 1,000,000
results：
142857

N = 10,000,000
results：
142857
1428570
1429857
Find the smallest number N in a given range num that meet the criteria:
N, 2N, 3N,.
N = 100,000,000
results：
142857
1428570
1429857
14285700
14298570
14299857
"""