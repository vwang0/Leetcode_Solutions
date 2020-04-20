/*
Find the smallest number N in a given range num that meet the criteria:
N, 2N, 3N, 4N, and 5N have the same digits.
*/
from collections import Counter
def findNum(num):
    for i in range(1,num):
        if Counter(str(i))== Counter(str(2*i))== Counter(str(3*i))== Counter(str(4*i))== Counter(str(5*i)):
            return i
        else:
            return 0