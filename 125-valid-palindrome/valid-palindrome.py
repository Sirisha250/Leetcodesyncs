import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Remove non-alphanumeric characters and convert to lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # Two-pointer check
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

# Example Usage:
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(sol.isPalindrome("race a car"))  # Output: False
print(sol.isPalindrome(" "))  # Output: True

        