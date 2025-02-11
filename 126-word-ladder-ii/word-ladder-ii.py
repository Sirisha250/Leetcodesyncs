from collections import deque, defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Step 1: BFS to find the shortest path layers
        parents = defaultdict(set)  # Graph to store parent nodes
        level = {beginWord}
        found = False

        while level and not found:
            next_level = defaultdict(set)
            for word in level:
                wordSet.discard(word)  # Remove visited words
                
            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            next_level[new_word].add(word)  # Build graph
                            if new_word == endWord:
                                found = True  # Stop BFS if endWord is reached

            level = next_level
            parents.update(next_level)  # Update parent relationships

        # Step 2: DFS to reconstruct all shortest paths
        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append([beginWord] + path[::-1])  # Reverse the path
                return
            for parent in parents[word]:
                dfs(parent, path + [word])

        if found:
            dfs(endWord, [])
        
        return res

# Example Usage:
sol = Solution()
print(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

print(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))
# Output: []
