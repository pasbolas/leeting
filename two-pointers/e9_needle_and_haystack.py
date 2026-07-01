'''
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    def strStr(haystack: str, needle: str) -> int:
        count = 0
        for i in range(len(haystack) - len(needle) + 1):
            count = 0
            for x in range(len(needle)):
                if haystack[i + x] == needle[x]:
                    count = count + 1
                else:
                    break
            if count == len(needle):
                return i
        return -1




print(Solution.strStr("abcd", "b"))

    

