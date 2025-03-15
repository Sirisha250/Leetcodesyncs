class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        
        rows, cols = len(board), len(board[0])
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    # Check if it's the start of a battleship
                    if (r == 0 or board[r - 1][c] == '.') and (c == 0 or board[r][c - 1] == '.'):
                        count += 1
                        
        return count
 