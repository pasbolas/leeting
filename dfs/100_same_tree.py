# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p,q):

            if (p == None and q == None):
                return True

            if (p == None and q is not None ):
                return False

            if (p is not None and q is None ):
                return False

            if (p is not None and q != None):
                if p.val == q.val:
                    return dfs(p.left, q.left) and dfs(p.right, q.right)
                elif (p.val != q.val):
                    return False
          
        return dfs(p,q)   