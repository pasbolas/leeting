'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        lastwordlength = 0
        length = 0
        length_tracker = 0
        
        prev_word = s[0]
        
        for word in s[1::]:
            if word == " " and prev_word != " ":
                length = length_tracker
                length_tracker = 0
                
            if word != " ":
                length_tracker+=1
        
        return length

print(Solution().lengthOfLastWord("Hello    hasda "))
        