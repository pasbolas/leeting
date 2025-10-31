
'''
PPROBLEM STATEMENT


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        smallest = min(strs, key=len)
        
        for word in strs:
            while smallest != "":
                if word.startswith(smallest):
                    break
                else:
                    smallest = smallest[:-1]
        
        return smallest