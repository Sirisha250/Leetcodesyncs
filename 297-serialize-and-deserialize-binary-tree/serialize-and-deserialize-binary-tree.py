import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = collections.deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = collections.deque([root])
        i = 1

        while queue:
            node = queue.popleft()
            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1

            if i < len(nodes) and nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1

        return root
