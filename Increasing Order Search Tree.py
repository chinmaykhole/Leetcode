class Solution:
    def increasingBST(self, root: TreeNode,tail=None) -> TreeNode:
        if not root:
            return tail
        result=self.increasingBST(root.left,root)
        root.left=None
        root.right=self.increasingBST(root.right,tail)
        return result
        