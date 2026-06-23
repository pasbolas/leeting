"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character 
in t (including duplicates) is included in the window. If there is 
no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

from collections import Counter, deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = deque([])

        minLength = float('inf')
        minWindow = deque([])
        need = Counter(t)
        windowCount = Counter()

        for item in s:

            window.append(item)
            windowCount[item] +=1 
            
            # while window is valid, subtract from left
            while windowCount >= need:
                if len(window) < minLength:
                    minLength = len(window)
                    minWindow = deque(window)
                leftItem = window.popleft()
                windowCount[leftItem] -= 1
        
        return ''.join(minWindow) 


# My earlier approach had Counter in the while loop, which had huge bottleneck because
# it counted everything again in the window.

# To tackle this, I made a live counter variable, and worked with it all along.