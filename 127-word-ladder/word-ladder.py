from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])  # (current word, transformation steps)

        while queue:
            word, length = queue.popleft()

            # Try all possible one-letter transformations
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    
                    if new_word == endWord:
                        return length + 1  # Found shortest path
                    
                    if new_word in wordSet:
                        queue.append((new_word, length + 1))
                        wordSet.remove(new_word)  # Mark as visited
            
        return 0  # If no path found

# Example Usage:
sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Output: 5
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))  # Output: 0

        