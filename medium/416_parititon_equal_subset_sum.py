"""Given an integer array nums, return true if you can partition 
the array into two subsets such that the sum of the elements in both
subsets is equal or false otherwise."""
from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums) // 2 # 22

        if sum(nums) % 2!= 0: ## pass
            return False
        
        # we are labelling a branch head here
        #memo = {}
        @lru_cache(maxsize = None)
        def dfs(elementIndex,currentSum, target):
            
            #if (elementIndex, currentSum) in memo:
                #return memo[elementIndex, currentSum]

            if currentSum == target:
                return True 
            elif currentSum > target or elementIndex >= len(nums):
                return False
            
            
            result =  dfs(elementIndex + 1, currentSum + nums[elementIndex], target) or dfs(elementIndex + 1, currentSum, target)

            # we label the head, any other function arriving looking for it's 
            # own possibility will see this and return, 
            # it won't explore it's own possibility that it wanted to look for
            # memo[(elementIndex, currentSum)] = result (got replaced by lru_cache)

            return result

        return dfs(0, 0, target)


            