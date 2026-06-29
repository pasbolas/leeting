"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        snowball_lr = 1
        snowball_rl = 1

        output = [0] * len(nums)

        for i in range(len(nums)):
            output[i] = snowball_lr
            snowball_lr = snowball_lr * nums[i]

        for i in range(len(nums)):
            output[-(i+1)] *= snowball_rl
            snowball_rl = snowball_rl * nums[-(i+1)]
        
        return output