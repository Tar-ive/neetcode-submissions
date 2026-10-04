# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # 4 possible combinations 
        # 1. p, q == root.val - return root.val 
        # 2. p, q are in root.right subtree -> only check that 
        # 3. p, q are in root.left subtree -> only check that 
        # 4. p, q are in different subtrees, return root 

        # need to write dfs for sure 

        # 1. p, q == root.val - return root.val 
        # if p.val or q.val == root.val: 
        #     return root 

        # def LCAhelper(node, a,b): 
        #     left = LCAhelper(node.left)
        #     right = LCAhelper(node.right)
        #     if node.left == a.val and node.right == b.val: 
        #         return node
            # should check descendants. 



            # what do we need the recursion to return here? LCA value

        # 2. p, q are in root.right subtree -> only check that
        # 3. p, q are in root.left subtree -> only check that 
        # 4. p, q are in different subtrees, return root 

        if p == q == Null: 
            return 
        curr = root
        while curr: 
            if p.val > curr.val and q.val > curr.val: 
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val: 
                curr = curr.left
            else: 
                return curr
            



        