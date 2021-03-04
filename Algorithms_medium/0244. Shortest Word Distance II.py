"""
0244. Shortest Word Distance II
Medium

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
class WordDistance:

    def __init__(self, words: List[str]):
        self.dic, self.l = {}, len(words)
        for i, w in enumerate(words):
            self.dic[w] = self.dic.get(w, []) + [i]

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.dic[word1], self.dic[word2]
        i = j = 0
        res = self.l
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)