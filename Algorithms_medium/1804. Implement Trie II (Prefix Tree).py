"""
1804. Implement Trie II (Prefix Tree)
Medium

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.
void erase(String word) Erases the string word from the trie.
 

Example 1:

Input
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
Output
[null, null, null, 2, 2, null, 1, 1, null, 0]

Explanation
Trie trie = new Trie();
trie.insert("apple");               // Inserts "apple".
trie.insert("apple");               // Inserts another "apple".
trie.countWordsEqualTo("apple");    // There are two instances of "apple" so return 2.
trie.countWordsStartingWith("app"); // "app" is a prefix of "apple" so return 2.
trie.erase("apple");                // Erases one "apple".
trie.countWordsEqualTo("apple");    // Now there is only one instance of "apple" so return 1.
trie.countWordsStartingWith("app"); // return 1
trie.erase("apple");                // Erases "apple". Now the trie is empty.
trie.countWordsStartingWith("app"); // return 0
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase.
It is guaranteed that for any function call to erase, the string word will exist in the trie.
"""
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.pcnt = 0
        self.cnt = 0
        
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        cur.pcnt += 1
        for ch in word:
            if cur.children[ord(ch) - ord('a')] == None:
                cur.children[ord(ch) - ord('a')] = Node()
            cur = cur.children[ord(ch) - ord('a')]
            cur.pcnt += 1
        cur.cnt += 1
        

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        flag = True
        for ch in word:
            if cur.children[ord(ch) - ord('a')] == None:
                flag = False
                break
            cur = cur.children[ord(ch) - ord('a')]
        return 0 if not flag else cur.cnt
    

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        flag = True
        for ch in prefix:
            if cur.children[ord(ch) - ord('a')] == None:
                flag = False
                break
            cur = cur.children[ord(ch) - ord('a')]
        return 0 if not flag else cur.pcnt
    

    def erase(self, word: str) -> None:
        cnt = self.countWordsEqualTo(word)
        if cnt:
            cur = self.root
            cur.pcnt -= 1
            for ch in word:
                cur = cur.children[ord(ch) - ord('a')]
                cur.pcnt -= 1
            cur.cnt -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)