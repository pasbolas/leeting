
"""

373. Find K Pairs with Smallest Sums
 -> Attempted
 -> Medium

You are given two integer arrays nums1 and nums2 sorted in 
non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the 
first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
"""

# First Approach
# absolutely memory eater plus, exceeds time limit

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        smallestPair =[]
        for item1 in nums1:
            for item2 in nums2:
                heapq.heappush(heap, [-(item1 + item2), [item1,item2]])
                if len(heap) > k:
                    heapq.heappop(heap)
                
        
        # removing everything other than k
        while len(smallestPair) < k:
            smallestPair.append(heapq.heappop(heap)[1])

        return smallestPair