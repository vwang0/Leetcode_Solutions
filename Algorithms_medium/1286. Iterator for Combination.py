"""
1286. Iterator for Combination
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
"""

class CombinationIterator:
    
    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.pos = [x for s in range(combinationLength)]
        self.finished = False

    def next(self) :
        ans = "".join([self.s[p] for p in self.pos])
        i = -1
        for k in range(len(self.pos) - 1, -1, -1):
            if self.pos[k] != len(self.s) - len(self.pos) + k:
                i = k
                break
        if i == -1:
            self.finished = True
        else:
            self.pos[i] += 1
            for j in range(i + 1, len(self.pos)):
                self.pos[j] = self.pos[j - 1] + 1
        return ans    

    def hasNext(self) :
        return not self.finished
        
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()