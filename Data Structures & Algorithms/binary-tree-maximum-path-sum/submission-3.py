# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # find sum of each path and keep running total which keeps updating
        res = [float("-inf")] #value of root 
    
        def maxSum(root):
            if not root: # edge cases 
                return 0
            leftMax = maxSum(root.left) # max sum of left subtree
            rightMax = maxSum(root.right)# max sum of left subtree
            leftMax = max(leftMax, 0) # making sure that leftMax are positive
            rightMax = max(rightMax, 0)
            res[0] = max(res[0], root.val + leftMax + rightMax)
# res[0] global max total
            return root.val + max(leftMax, rightMax)# max of either best extendable downward path

        maxSum(root)
        return res[0]

        