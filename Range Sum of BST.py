class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans+=node.val
                if node.val > L:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        dfs(root)
        return self.ans
                    
                    
                    
    
            
        