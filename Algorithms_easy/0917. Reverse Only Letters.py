"""
0917. Reverse Only Letters
Easy

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
"""
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i, j, LS = 0, len(S)-1, list(S)
        while i < j:
            if not LS[i].isalpha():
                i += 1
            elif not LS[j].isalpha():
                j -= 1 
            else:
                LS[i], LS[j] = LS[j], LS[i]
                i, j = i + 1, j - 1
        return ''.join(LS)


        