/*
Find the smallest number N in a given range num that meet the criteria:
N, 2N, 3N, 4N, and 5N have the same digits.
*/
from collections import Counter
def findNum(N):
    for i in range(1,N):
        if Counter(str(i))== Counter(str(2*i)) and Counter(str(2*i)) == Counter(str(3*i)) and Counter(str(3*i)) == Counter(str(4*i)) and Counter(str(4*i)) == Counter(str(5*i)):
            return i
    return print('Not Found!')