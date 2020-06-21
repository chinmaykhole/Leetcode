class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root and (root == p or root == q):
            return root
        
        if not root:
            return None
        
        else:
            left_ancestor=self.lowestCommonAncestor(root.left,p,q)
            right_ancestor=self.lowestCommonAncestor(root.right,p,q)
            
            if left_ancestor and right_ancestor:
                return root
            elif left_ancestor:
                return left_ancestor
            elif right_ancestor:
                return right_ancestor
            else:
                return None