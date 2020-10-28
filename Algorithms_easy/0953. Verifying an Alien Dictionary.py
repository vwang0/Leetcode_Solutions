"""
953. Verifying an Alien Dictionary
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = {}
        for i, c in enumerate(order):
            dic[c] = i
        for i in range(len(words)-1):
            cur = words[i]
            nex = words[i+1]
            for j in range(min(len(cur), len(nex))):
                if cur[j] != nex[j]:
                    if dic[cur[j]] > dic[nex[j]]:
                        return False
                    break
            else:
                if len(cur) > len(nex):
                    return False
        return True



class Solution:
    def isAlienSorted(self, words, order):
        alien_dic = {}
        # create alien dictionary by using enumerate
        for i, c in enumerate(order):
            alien_dic[c] = i

        dic_order = sorted(words, key=lambda x: [alien_dic[c] for c in x])
        return dic_order == words

class Solution:
    def isAlienSorted(self, words, order):
            return words == sorted(words, key=lambda w: map(order.index, w))
            