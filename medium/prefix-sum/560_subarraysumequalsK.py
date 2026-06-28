class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        count = 0

        for item in nums:
            prefix = prefix + item
            count += seen.get(prefix - k, 0)
            seen[prefix] = seen.get(prefix, 0) + 1
        
        return count
        



# print(Solution().subarraySum([1,2,3],3))

        