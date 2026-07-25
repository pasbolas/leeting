class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # our input is empty
        # our input is a string

        numSet = set()
        
        for item in nums:
            if item in numSet: # O(1)
                return True
            else:
                numSet.add(item)
        
        return False