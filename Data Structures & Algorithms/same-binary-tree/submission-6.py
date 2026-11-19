# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(pNode, qNode):
            if not pNode and not qNode:
                return True
            if pNode and qNode and pNode.val == qNode.val:
                return helper(pNode.left, qNode.left) and helper(pNode.right, qNode.right)
            return False
        return helper(p, q)