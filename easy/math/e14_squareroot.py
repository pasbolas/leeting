
## solution v1
## i hate this solution, this pretty brute force
class Solution:
    def mySqrt(x: int) -> int:
        i = 0
        for i in range(0,x + 1):
            if i*i > x:
                return i - 1 
        return i
print(Solution.mySqrt(1))