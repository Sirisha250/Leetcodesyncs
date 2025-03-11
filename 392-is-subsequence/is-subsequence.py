class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move s pointer
                i += 1
            j += 1  # Always move t pointer
        
        return i == len(s)  # Check if we matched all of s
