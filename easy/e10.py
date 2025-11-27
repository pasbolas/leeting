'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''

# incomplete question

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search_recursive(arr, low, high, target):

            mid = (low + high) // 2

            if low > high:
                return low
            
            if arr[mid] == target:
                return mid
            
            elif arr[mid] < target:
                # search right
                return binary_search_recursive(arr, mid + 1, high, target)
            
            else:
                # search the left side of the array
                return binary_search_recursive(arr, low, mid - 1, target)
            
        return binary_search_recursive(nums,0, len(nums) - 1, target )


arr= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19]
target = 18

print(Solution().searchInsert( arr, target))