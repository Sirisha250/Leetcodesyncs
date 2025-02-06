class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index):
            if index == len(word):  # If all letters are found
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]  # Save the original character
            board[r][c] = "#"  # Mark as visited
            
            # Explore all 4 possible directions
            found = (dfs(r+1, c, index+1) or
                     dfs(r-1, c, index+1) or
                     dfs(r, c+1, index+1) or
                     dfs(r, c-1, index+1))
            
            board[r][c] = temp  # Restore original character
            return found
        
        # Start DFS from each cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):  
                    return True  # If found, return immediately
        
        return False  # If not found, return False

# Example test cases
solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))  # Output: True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))     # Output: True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))    # Output: False

        