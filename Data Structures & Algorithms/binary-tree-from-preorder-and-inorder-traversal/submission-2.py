# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p = deque(preorder) # beause we will be popping from queue while before adding to treenode 
        n= len(preorder) # or postorder 
        lookup = {v:i for i,v in enumerate(inorder)} # made value as key, index as value so we can do lookup of index

        def recursion(start, end): 
            # base case 
            if start > end: 
                return None 
            else: 
                candidate = p.popleft()
                root = TreeNode(candidate) # Builds root node 
                # use inorder to find what to put in left and right 
                # for that we need lookup of index of inorder 
                middle = lookup[candidate]
                #start building tree
                root.left = recursion(start, middle -1)
                root.right= recursion(middle+1, end)
                return root 
        return recursion(0, n-1)
