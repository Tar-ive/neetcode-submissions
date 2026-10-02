# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, CurSum): 
            if not node:  # checking for empty tree 
                return False 
            
            CurSum += node.val # adding current node value to current sum
            if not node.left and not node.right: # if it is at root node 
                return CurSum == targetSum 
            
            return (dfs(node.left, CurSum) or
            dfs(node.right, CurSum)) 
        return dfs(root, 0)
        