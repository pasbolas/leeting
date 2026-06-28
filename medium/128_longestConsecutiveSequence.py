"""

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

"""
# sorry guys for the absolute debug mayhem, I just learned dfs and for fucks sake I can't stop using recursion in everything
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA, help(help(help(help(help)))
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLength = 0

        

        def counter(number, consecutiveCount):
            print(f"Is {number} in seen?")
            if (number) in seen:
                consecutiveCount += 1
                print(f"Yes : ConsecutiveCount : {consecutiveCount}")
                consecutiveCount = counter(number + 1 , consecutiveCount)
                
            
            print(f"No, returning...{consecutiveCount}")
            return consecutiveCount

        for item in seen:
            currentLength = 0
            print(f"Is {item - 1} in seen? ")
            if (item - 1) not in seen:
                print(f" {item - 1} is not in seen, going balls deep... ")
                currentLength = counter(item, 0)
            else:
                print(f"  yes : {item - 1}, well this is not the first element, wa wa wa..")
            print(f"CurrentLength : {currentLength}")
            maxLength = max(currentLength, maxLength)
            print(f"MaxLength = {maxLength}")

            print("-------")
        
        return maxLength



    # Less mayhem, version, plomiseee
    def longestConsecutive_less_bad_plomiseee_uWu(self, nums: List[int]) -> int:
        
        seen = set(nums)
        maxLength = 0

        for item in seen:
            currentCounter = 0
            currentItem = item
            if (currentItem - 1) not in seen:
                while ((currentItem) in seen) :
                    currentCounter += 1
                    currentItem += 1
            
                maxLength = max(currentCounter, maxLength )
        
        return maxLength

        


# {1, 2, 3, 100, 4, 200}
print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive_less_bad_plomiseee_uWu([100,4,200,1,3,2]))