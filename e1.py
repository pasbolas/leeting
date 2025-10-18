class Solution:
    def isPalindrome(x: int) -> bool:
        string_word = str(x)
        rev_string_word = string_word[::-1]
        if string_word == rev_string_word:
            return True
        return False
        

print(Solution.isPalindrome(122321))