class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        if self.isBalanced(root.left) == True and self.isBalanced(root.right) == True and abs(height(root.left) - height(root.right)) <= 1:
            return True
        else:
            return False
