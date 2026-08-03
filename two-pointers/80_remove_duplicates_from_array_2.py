"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

from collections import deque
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # this can be solved using stack, but there is an extra memory contraint, so we will use two pointers
        
        # stack = deque([nums[0]])
        # count = 1

        # i = 1
        # while i < len(stack):
        #     # check if item already in stack
        #     while stack[-1] == nums[i]:
        #         i += 1

        #     #add the first item to stack
        #     stack.append(nums[i])
        #     count += 1
        #     i += 1

        anchor, explorer = 0,0

        while explorer < len(nums):
            
            if anchor < 2 or nums[anchor - 2] != nums[explorer]:
                nums[anchor] = nums[explorer]
                anchor += 1
            
            explorer += 1
                
        return anchor