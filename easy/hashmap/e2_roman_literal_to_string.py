# Converting roman literal(string) to numbers(int)


# never put dict in another function, alwasy use it raw, it makes it faster
class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_dict = {
        "I":1,
        "V":5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

        list1 = []
        sum = roman_dict[s[-1]]
        
        for j in range(len(s) - 1):

            cur = roman_dict[s[j]]
            next1 = roman_dict[s[j+1]]

            if cur > next1 or cur == next1:
                sum += cur
            else:
                sum -= cur

        return sum
