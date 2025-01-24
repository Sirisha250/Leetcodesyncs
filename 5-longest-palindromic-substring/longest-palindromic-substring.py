class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Helper function to expand around the center
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring
            return s[left + 1:right]
        
        if len(s) < 1:
            return ""
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            # Odd length palindromes (center is a single character)
            palindrome1 = expand_around_center(i, i)
            # Even length palindromes (center is between two characters)
            palindrome2 = expand_around_center(i, i + 1)
            
            # Update the longest palindrome
            longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)
        
        return longest_palindrome

# Test cases
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(solution.longestPalindrome("cbbd"))   # Output: "bb"

        