class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        
        # Count frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Find the first character that appears less than k times
        for char in s:
            if freq[char] < k:
                # Split the string at this character and check both parts
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
        
        # If all characters meet the condition, return the full string length
        return len(s)

# Test Cases
solution = Solution()
print(solution.longestSubstring("aaabb", 3))  # Output: 3
print(solution.longestSubstring("ababbc", 2))  # Output: 5
