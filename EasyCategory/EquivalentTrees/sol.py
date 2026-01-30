# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            #do a dfs on both trees at the same time while comparing vals

            #reached null, must mean they are identical
            if not node1 and not node2:
                return True

            #if one is empty or values are not equivalent, it is not identical
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            #dfs step
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        return dfs(p,q)
