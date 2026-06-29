"""
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.
"""

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        totalCount = Counter(nums)
        heap=[]

        for item in totalCount:
            heapq.heappush(heap, [totalCount[item], item])
        
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        totalList=[]
        for item in heap:
            totalList.append(item[1])
        
        return totalList  