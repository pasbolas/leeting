# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            
            leftCount,rightCount = 0,0

            if root.left:
                leftCount = dfs(root.left)
            if root.right:
                rightCount = dfs(root.right)
            
            return 1 + max(leftCount, rightCount)
        
        return dfs(root)