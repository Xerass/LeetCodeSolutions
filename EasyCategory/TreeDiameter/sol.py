# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #perform a dfs and store path length

        maxDiameter = 0

        def getHeight(node):
            #give it access to maxdim
            nonlocal maxDiameter
            if not node:
                return 0

            leftH = getHeight(node.left)
            rightH = getHeight(node.right)

            #potential diameter is left + right heights
            #compare to curr so we cna always find max

            maxDiameter = max(maxDiameter, leftH + rightH)

            #return is hights of either (choose max) plus curr node
            return 1 + max(leftH, rightH)
        
        getHeight(root)
        return maxDiameter
