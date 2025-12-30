# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #recursive sol
        def invert(node):
            if node is None:
                return

            #swap
            node.right, node.left = node.left, node.right
            #recurse
            invert(node.right)
            invert(node.left)


        invert(root)
        return root
