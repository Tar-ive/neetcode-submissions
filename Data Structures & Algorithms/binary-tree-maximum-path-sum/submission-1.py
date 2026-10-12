# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # find sum of each path and keep running total which keeps updating
        res = [root.val]
    
        def maxSum(root):
            if not root: 
                return 0
            leftMax = maxSum(root.left)
            rightMax = maxSum(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        maxSum(root)
        return res[0]

        