class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)  # Convert wordDict to a set for O(1) lookups
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: Empty string can be segmented

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # No need to check further once True

        return dp[len(s)]

# Example usage:
solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))  # Output: True
print(solution.wordBreak("applepenapple", ["apple", "pen"]))  # Output: True
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False
