# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = 1

        def dfs(node): 
            if not node: 
                return [True, 0]

            max_left = dfs(node.left)
            max_right = dfs(node.right)
            balance = (max_left[0] and max_right[0] and abs(max_left[1] - max_right[1]) <= 1)
            return [balance, 1+ max(max_left[1], max_right[1])]
        
        return dfs(root)[0]
        