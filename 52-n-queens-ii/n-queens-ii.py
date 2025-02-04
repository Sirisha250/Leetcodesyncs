class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def backtrack(row, cols, diagonals, anti_diagonals):
            if row == n:
                self.count += 1
                return
            
            for col in range(n):
                diag = row - col
                anti_diag = row + col

                if col in cols or diag in diagonals or anti_diag in anti_diagonals:
                    continue

                cols.add(col)
                diagonals.add(diag)
                anti_diagonals.add(anti_diag)

                backtrack(row + 1, cols, diagonals, anti_diagonals)

                cols.remove(col)
                diagonals.remove(diag)
                anti_diagonals.remove(anti_diag)

        self.count = 0
        backtrack(0, set(), set(), set())
        return self.count

        