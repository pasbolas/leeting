# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def traversal(rootNode, result):
            if rootNode is None:
                return result
            if rootNode.left:
                traversal(rootNode.left, result)
            result.append(rootNode.val) 
            if rootNode.right:
                traversal(rootNode.right, result)
            
            return result
        
        output = traversal(root, [])

        return output