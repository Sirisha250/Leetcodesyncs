class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None (modifies s in-place)
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]  # Swap characters
            left += 1
            right -= 1

        