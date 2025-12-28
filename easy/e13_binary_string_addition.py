"""

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""

class Solution:
    def addBinary( a: str, b: str) -> str:

        # adding padding to the smallest 
        len_a = len(a)
        len_b = len(b)

        biggest_len = len_a if len_a > len_b else len_b

        if len_a > len_b:
            b = b.rjust(biggest_len, "0")
        else:
            a = a.rjust(biggest_len, "0")
        
        carry = 0
        result = ""

        # sum becomes both numbers added plus carry, carry can be at max 1
        for i in range(biggest_len - 1, -1, -1):

            b_sum = int(a[i]) + int(b[i]) + carry
            result += "0" if b_sum % 2 == 0 else "1"

            carry = 1 if b_sum >= 2 else 0
        
        if carry == 1: result+="1"

        print(result[::-1])
        return (result[::-1])



