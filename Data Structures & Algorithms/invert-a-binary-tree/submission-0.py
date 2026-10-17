from typing import Optional




class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap the left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root