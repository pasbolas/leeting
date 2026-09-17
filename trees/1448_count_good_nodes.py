# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given a binary tree root, a node X in the tree is 
# named good if in the path from root to X there are 
#no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, biggest):
            
            count = 0

            countLeft, countRight = 0,0

            if node.val >= biggest:
                count += 1
                biggest = node.val
            
            
            if node.left:
                countLeft = dfs(node.left, biggest)
            if node.right:
                countRight = dfs(node.right, biggest)
            
            count += countLeft + countRight
            
            return count

        return dfs(root, -float('inf'))

        