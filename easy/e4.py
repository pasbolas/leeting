# Write a function to find the longest common prefix string amongst an array of stri
# If there is no common prefix, return an empty string 

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        leng = len(strs)
        subset = []
        for i in range(leng):
            subset.append(strs[0:i - 1])
        print(subset)
        return "a"

        
    
print(Solution.longestCommonPrefix(["flower","flow","flight"]))

