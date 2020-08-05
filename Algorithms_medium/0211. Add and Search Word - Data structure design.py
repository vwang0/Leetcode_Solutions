"""
0211. Add and Search Word - Data structure design
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

class TreeNode(object):
    def __init__(self, val):
        self.children = {}
        self.end_here = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(-1)


    def addWord(self, word: str) :
        """
        Adds a word into the data structure.
        """
        trav = self.root
        for i, c in enumerate(word):
            if c in trav.children:
                trav = trav.children[c]
            else:
                trav.children[c] = TreeNode(c)
                trav = trav.children[c]
            if i == len(word) - 1:
                trav.end_here = True

    def search(self, word: str) :
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(i, trav):
            if i == len(word):
                return trav.end_here
            if word[i] != ".":
                if word[i] not in trav.children:
                    return False
                else:
                    return dfs(i + 1, trav.children[word[i]])
            else:
                for val in trav.children.values():
                    if dfs(i + 1, val):
                        return True
                return False

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)