"""An ugly number is a positive integer whose prime 
factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number."""

import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        count = 0
        visited = set([1])
        while 1:
            item = heapq.heappop(heap)

            count +=1

            if count == n:
                return item

            if item*2 not in visited:
                heapq.heappush(heap, item*2)
                visited.add(item*2)
            if item*3 not in visited:
                heapq.heappush(heap, item*3)
                visited.add(item*3)
            if item*5 not in visited:
                heapq.heappush(heap, item*5)
                visited.add(item*5)

            

        