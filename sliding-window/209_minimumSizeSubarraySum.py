"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater 
than or equal to target.
If there is no such subarray, return 0 instead.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        minLength = float(inf)
        windowSum = 0

        for right in range(len(nums)):

            windowSum += nums[right]

            while windowSum >= target:
                length = right - left + 1
                minLength = min(minLength, length)
                windowSum -= nums[left]
                left += 1
                
            
        return minLength if minLength != float(inf) else 0
                
            

