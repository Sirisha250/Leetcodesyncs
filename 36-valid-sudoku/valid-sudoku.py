class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3x3 boxes indexed as (row//3)*3 + (col//3)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue  # Skip empty cells
                
                box_index = (r // 3) * 3 + (c // 3)
                
                # Check for duplicates in row, column, and box
                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    return False

                # Add the number to the respective sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
        
        return True  # No conflicts found

       