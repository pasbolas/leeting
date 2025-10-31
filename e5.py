array1 = [2,5,7,8,9,2,3,4,3,1]

class Solution:
    def hasIncreasingSubarrays(nums: List[int], k: int) -> bool:
        last_temp_count = 0

        last_num = nums[0]
        longest = 1
        current_longest = 1

        for index, element in enumerate(nums):
            for current_number in nums[1:]:
                if last_num > current_number:
                    current_longest += 1
                else:
                    longest = max(current_longest, longest)
                    current_longest = 1

        return True if k == last_temp_count else False

print(Solution.hasIncreasingSubarrays(array1, 3))

