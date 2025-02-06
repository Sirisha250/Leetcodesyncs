from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        t_count = Counter(t)  # Frequency map of t
        window_count = {}  # Frequency map for the current window
        required_chars = len(t_count)  # Number of unique chars in t that must be present in window
        formed_chars = 0  # Number of unique chars in window that meet the required frequency
        
        l, r = 0, 0  # Sliding window pointers
        min_len = float('inf')
        min_window = ""

        while r < len(s):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1
            
            # If the current character's frequency matches the required frequency, increase formed_chars
            if char in t_count and window_count[char] == t_count[char]:
                formed_chars += 1

            # Try to shrink the window while it's valid
            while l <= r and formed_chars == required_chars:
                current_window_size = r - l + 1
                if current_window_size < min_len:
                    min_len = current_window_size
                    min_window = s[l:r+1]

                # Remove the leftmost character
                left_char = s[l]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed_chars -= 1  # We removed a necessary char, so decrement formed_chars

                l += 1  # Move left pointer forward
            
            r += 1  # Move right pointer forward
        
        return min_window
