class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        :type board: List[List[int]]
        :rtype: None
        """
        rows, cols = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Step 1: Determine the next state
        for r in range(rows):
            for c in range(cols):
                live_neighbors = sum(1 for dr, dc in directions
                                     if 0 <= r + dr < rows and 0 <= c + dc < cols and abs(board[r + dr][c + dc]) == 1)

                # Apply rules using the markers (-1 and 2)
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  # Alive → Dead
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2  # Dead → Alive

        # Step 2: Final transformation (-1 → 0, 2 → 1)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1

        