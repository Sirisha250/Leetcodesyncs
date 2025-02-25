class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        temp = s + "#" + s[::-1]  # Create a new string with a separator
        lps = [0] * len(temp)  # KMP prefix array
        
        # Build LPS array
        j = 0
        for i in range(1, len(temp)):
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            if temp[i] == temp[j]:
                j += 1
            lps[i] = j
        
        # The longest palindromic prefix length
        longest_pal_prefix = lps[-1]
        
        # Remaining suffix that needs to be added in front
        return s[::-1][:len(s) - longest_pal_prefix] + s
