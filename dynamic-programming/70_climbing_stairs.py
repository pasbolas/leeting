"""
You are climbing a staircase. 
It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        step = 0
        
        if n == 1: return 1
        if n == 2: return 2

        waysbefore = 2
        waysbeforebefore = 1

        for step in range(3, n + 1):

            current = waysbefore + waysbeforebefore
                
            waysbeforebefore = waysbefore
            waysbefore = current
        
        return current