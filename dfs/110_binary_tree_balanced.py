# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            leftHeight = 0

            if not root:
                return True

            if root.left:
                leftHeight = dfs(root.left)
            
            rightHeight = 0
            if root.right:
                rightHeight = dfs(root.right)
            
            if leftHeight is False or rightHeight is False:
                return False

            heightDiff = rightHeight - leftHeight

            if abs(heightDiff) > 1:
                return False


            return max(leftHeight, rightHeight) + 1 
        
        height = dfs(root)
        if height == False:
            return False
        else:
            return True    