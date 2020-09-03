"""
0744. Find Smallest Letter Greater Than Target
Easy
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if not letters: return None
        letters.sort()
        for ch in letters:
            if ch > target:
                return ch
        return letters[0]

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if not letters: return None
        n = len(letters)
        low = 0
        high = n - 1
        result = 0

        while low <= high:
            mid = low + (high - low) // 2
            if letters[mid] > target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return letters[result]