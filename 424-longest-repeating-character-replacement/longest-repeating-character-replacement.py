from collections import Counter

class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = Counter()  # To store character frequencies
        max_freq = 0       # Most frequent character count in the window
        left = 0           # Left pointer of the sliding window
        max_length = 0     # Result variable
        
        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])  
            
            # Check if window size - most frequent character > k
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1  # Shrink the window
            
            max_length = max(max_length, right - left + 1)  # Update result
        
        return max_length
