"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preDict = defaultdict(list)
        visiting = set()

        # we got a dict with list as value for a key
        for a,b in prerequisites:
            preDict[a].append(b)

        safe = set()
        
        def dfs(father):

            if father in safe:
                return True

            if father in visiting:
                return False
            
            visiting.add(father)

            for child in preDict[father]:
                status = dfs(child)
                if status == False:
                    return False
                
            safe.add(father)

            visiting.remove(father)      
            return True



        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        
        return True