class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def is_safe(row, col, queens):
            for r, c in queens:
                if c == col or abs(r - row) == abs(c - col):
                    return False
            return True

        def backtrack(row, queens):
            if row == n:
                board = []
                for r, c in queens:
                    line = ['.'] * n
                    line[c] = 'Q'
                    board.append("".join(line))
                solutions.append(board)
                return

            for col in range(n):
                if is_safe(row, col, queens):
                    queens.append((row, col))
                    backtrack(row + 1, queens)
                    queens.pop()

        solutions = []
        backtrack(0, [])
        return solutions

        