class Solution(object):
    def findSubstringInWraproundString(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        dp = [0] * 26  # Stores the max length of substrings ending at each letter
        max_length = 0  # Length of the current valid substring sequence
        
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or (s[i - 1] == 'z' and s[i] == 'a')):
                max_length += 1
            else:
                max_length = 1  # Reset for new start
            
            index = ord(s[i]) - ord('a')
            dp[index] = max(dp[index], max_length)
        
        return sum(dp)  # Sum up all max substrings
