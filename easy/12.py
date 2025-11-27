'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for num in digits:
            string += str(num)
        num_string = int(string)
        num_string = num_string + 1
        string_num = str(num_string)

        array = []
        for word in string_num:
            array.append(int(word))
        return array
        
