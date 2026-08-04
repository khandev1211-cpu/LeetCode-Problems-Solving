class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = None
        self.second = None
        self.prev = None
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.prev and self.prev.val > root.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.inorder(root.right)