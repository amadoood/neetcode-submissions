# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(root, otherRoot):
            if not root and not otherRoot:
                return True
            if root and otherRoot and root.val == otherRoot.val:
                return isSameTree(root.left, otherRoot.left) and isSameTree(root.right, otherRoot.right)
            return False
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False