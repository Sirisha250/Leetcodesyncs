from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = Counter(s)
        length = 0
        odd_found = False

        for count in char_count.values():
            length += count if count % 2 == 0 else count - 1
            if count % 2 == 1:
                odd_found = True

        return length + 1 if odd_found else length
    