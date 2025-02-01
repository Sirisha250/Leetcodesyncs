class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None. Modifies board in-place.
        """
        # Hash sets to track used numbers in rows, cols, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize sets with existing numbers and store empty cells
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != ".":
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)
                else:
                    empty_cells.append((r, c))

        def solve(index):
            """Backtracking function to solve Sudoku."""
            if index == len(empty_cells):  # All cells filled, solution found
                return True
            
            r, c = empty_cells[index]
            box_index = (r // 3) * 3 + (c // 3)
            
            for num in map(str, range(1, 10)):  # Try numbers 1-9
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                    # Place number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

                    # Recurse to next cell
                    if solve(index + 1):
                        return True

                    # Backtrack if no solution
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_index].remove(num)
            
            return False  # No valid number found
        
        solve(0)
