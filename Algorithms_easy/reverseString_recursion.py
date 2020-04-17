"""
reverse string with recursion

"""
def reverseString(s):
    def helper(start, end, ls):
        if start >= end:
            return
        ls[start], ls[end] = ls[end], ls[start]
    return helper(0, len(s)-1, s)