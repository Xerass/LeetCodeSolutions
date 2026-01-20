# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #perform a dfs, but this time, instead of replacing a var called max, we just compare each return to see if they are within +- 1 of each other
        def dfs(node):
            #base case
            if not node:
                return 0
            

            l_height = dfs(node.left)
            if l_height  == -1:
                #node is unbalanced
                return -1
            
            r_height = dfs(node.right)
            if r_height == -1:
                return -1           
            #actual unbalanced check
            if abs(l_height - r_height) > 1:
                #if difference is outside 1, unbalanced
                return -1
            
            #if balanced return actual height
            return max(l_height,r_height) + 1
        
        return dfs(root) != -1
            
