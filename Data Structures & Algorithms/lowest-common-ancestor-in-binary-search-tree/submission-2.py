# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # recursive solution 
        # we need to check what lowest common ancestor is: 
        # we can have 4 conditions
        # both null - return root 
        # if they are in left subtree, root of left subtree 
        # if both p and q > root they are both in right subtree, root of right subtree 
        # if they are in 2 different branches, root of where they split from. 
        # if p or q == root: 
        # return root.val # as this is the LCA

        # i dont remember if we do bfs or dfs in this problem but remember that it is recursion 
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

        

         

        
        