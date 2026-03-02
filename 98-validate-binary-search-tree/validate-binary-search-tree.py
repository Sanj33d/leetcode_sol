# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            # bc
            if node == None:
                return True
            # bc2
            checker = low < node.val < high
            if checker == False:
                return False
            
            left_rec = dfs(node.left, low, node.val)
            right_rec = dfs(node.right, node.val, high)

            return left_rec and right_rec
        ans = dfs(root, float('-inf'), float('inf'))
        return ans
        