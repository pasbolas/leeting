"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalList = defaultdict(list)
        setList = []
        for item in strs:
            hashableItem = "".join(sorted(item))
            finalList[hashableItem].append(item)
        
        for item in finalList:
            setList.append(finalList[item])

        return setList
