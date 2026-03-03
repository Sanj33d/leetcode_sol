# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #bc1
        if root is None:
            return
        #bc2
        elif root == p or root == q:
            return root
        #rc
        left_rc = self.lowestCommonAncestor(root.left, p,q)
        right_rc = self.lowestCommonAncestor(root.right, p,q)

        if left_rc != None and right_rc != None:
            return root
        elif left_rc != None:
            return left_rc
        else:
            return right_rc

            
            
        
        