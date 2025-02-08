class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = None

    def recoverTree(self, root):
        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev and node.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = node

            self.prev = node  
            inorder(node.right)

        inorder(root)

        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val

