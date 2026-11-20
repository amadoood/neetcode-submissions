# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        result.append([root.val])

        queue = deque([root])
        while queue:
            currentLevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    currentLevel.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    currentLevel.append(node.right.val)
            if currentLevel:
                result.append(currentLevel)
            
        return result
        