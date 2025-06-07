# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # bottom-up approach (recursion then operation)
        diameter = 0

        def helper(root): # calculates height
            nonlocal diameter # nonlocal = global
            if root is None: #bc
                return 0
            else:
                l_traversal = helper(root.left) #lrc
                r_traversal = helper(root.right) #rrc
                
                height = 1 + max(l_traversal, r_traversal) #op
                diameter = max(diameter, l_traversal + r_traversal)
                return height #op

        ans = helper(root)
        return diameter

            
            

        
