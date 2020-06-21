# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(root):
            
            nonlocal maxDiameter
            if not root:
                return False
            left=depth(root.left)
            right=depth(root.right)
            
            currentDiameter=left+right
            
            maxDiameter = max(maxDiameter,currentDiameter)
            
            return max(left,right)+1
        maxDiameter=0
        depth(root)
        return maxDiameter