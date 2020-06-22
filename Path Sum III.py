# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        return self.helper(root,s,[s])
    
    def helper(self,node,origin,targets):
        if not node:
            return 0
        hit=0
        for t in targets:
            if not t-node.val:
                hit+=1
        targets=[t-node.val for t in targets]+[origin]
        return hit + self.helper(node.left,origin,targets) + self.helper(node.right,origin,targets)
                
        
        
        
        