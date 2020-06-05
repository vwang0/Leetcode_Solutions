"""
0269. Alien Dictionary
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def dfs(i):
            seen[i] = 0
            for nei in graph[i]:
                if nei in seen:
                    if seen[nei] == 0:
                        return False
                else:
                    if not dfs(nei):
                        return False
            seen[i] = 1
            res.appendleft(i)
            return True
        
        # records all characters appeared in words
        nodes = set()
        for word in words:
            nodes |= set(word)
        
        # construct the graph
        graph = collections.defaultdict(set)
        for i in range(len(words)-1):
            k = 0
            while k < len(words[i]) and k < len(words[i+1]):
                if words[i][k] != words[i+1][k]:
                    graph[words[i][k]].add(words[i+1][k])
                    break
                else:
                    k += 1
        
        # topologically sort the characters
        res = collections.deque()
        seen = {}
        for i in nodes:
            if i not in seen:
                if not dfs(i):
                    return ""
        return "".join(res)


def alienOrder(self, words):
    pre, suc = collections.defaultdict(set), collections.defaultdict(set)
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                suc[a].add(b)
                pre[b].add(a)
                break
    chars = set(''.join(words))
    free = chars - set(pre)
    order = ''
    while free:
        a = free.pop()
        order += a
        for b in suc[a]:
            pre[b].discard(a)
            if not pre[b]:
                free.add(b)
    return order * (set(order) == chars)


def alienOrder(self, words):
    less = []
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                less += a + b,
                break
    chars = set(''.join(words))
    order = []
    while less:
        free = chars - set(zip(*less)[1])
        if not free:
            return ''
        order += free
        less = filter(free.isdisjoint, less)
        chars -= free
    return ''.join(order + list(chars))




