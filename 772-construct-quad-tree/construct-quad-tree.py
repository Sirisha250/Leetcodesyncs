class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def isUniform(x, y, size):
            """Check if all values in a subgrid are the same"""
            val = grid[x][y]
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != val:
                        return False, None
            return True, val

        def build(x, y, size):
            """Recursively build the Quad-Tree"""
            uniform, val = isUniform(x, y, size)
            if uniform:
                return Node(val == 1, True)
            
            half = size // 2
            return Node(
                True, False,
                build(x, y, half),                   # Top Left
                build(x, y + half, half),            # Top Right
                build(x + half, y, half),            # Bottom Left
                build(x + half, y + half, half)      # Bottom Right
            )

        return build(0, 0, len(grid))
