# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # need to do dfs 
        # and then keep adding count 
        #lets do recursive
        # how to iterate over and work with this problem? 

        def dfs_recursive(node):
            if not node:
                return 0 

            left_depth = dfs_recursive(node.left)
            right_depth = dfs_recursive(node.right)

            return 1 + max(left_depth, right_depth)  
            
        return dfs_recursive(root)


        