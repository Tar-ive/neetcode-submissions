# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Inorder = Left -> Root -> Right 
        # for eg = 1, 2, 3, 4, 5, 6, 7 
        # Check left subtree => [2, 4, 5] -> traverse in that order 
        # Check root 
        # Check right subtree => [3, 6, 7] -> traverse in that order 
        # answer is -> [4,2,5,1,6,3,7]

        # 1. create result list 
        # 2. define recursive helper 
        # 3. if node == null return (base case)
        # 4. recursively call = left child 
        # 5. check current node's value (root)
        # 6. recursively call = right child 
        # 7. return result after traversing entire tree 

        result = []

        def dfs(node): 
            if not node: 
                return 
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result 



        