"""
0249. Group Shifted Strings
Medium

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        key = lambda s: [(ord(c) - ord(s[0])) % 26 for c in s]
        return [list(g) for _, g in itertools.groupby(sorted(strings, key=key), key)]

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                circular_difference = 26 + ord(s[i+1]) - ord(s[i])
                key += (circular_difference % 26,)
            hashmap[key] = hashmap.get(key, []) + [s]
        return list(hashmap.values())        