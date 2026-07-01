"""
Given the root of a binary tree, return the level 
order traversal of its nodes' values. 
(i.e., from left to right, level by level).
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        answer = []
        while queue:
            length = len(queue)
            currentWindow = []
            for _ in range(length):  
                grab = queue.popleft()
                currentWindow.append(grab.val)
                if grab.left:
                    queue.append(grab.left)
                if grab.right:
                    queue.append(grab.right)   
                
            answer.append(currentWindow)


        return answer