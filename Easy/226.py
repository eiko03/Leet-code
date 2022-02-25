# Invert Binary tree

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root:
            temp_right =root.right
            root.right =root.left
            root.left =temp_right

            self.invertTree(root.left)
            self.invertTree(root.right)

        return root