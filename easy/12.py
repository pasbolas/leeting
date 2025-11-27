'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''


class Solution:
    def plusOne(self, digits):

        i = len(digits) - 1
        
        while i >= 0:

            # add one if the digit is < 9 and return the value otherwise if its 9 put 0 in place of it
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            i -= 1
            print(digits)
        
        # this is a nuke button in case all digits are 9
        return [1] + digits


print(Solution().plusOne([1,0,9]))
        
