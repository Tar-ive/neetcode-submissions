# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root): 
            if not root: 
                return 0 
            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)
            maxLeft = max(0, maxLeft)
            maxRight = max(0, maxRight)

            res[0] = max(res[0], root.val+ maxLeft+maxRight)

            return root.val+max(maxLeft, maxRight)

        dfs(root)
        return res[0]