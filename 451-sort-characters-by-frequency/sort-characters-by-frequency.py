from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count the frequency of each character
        freq = Counter(s)
        
        # Sort characters by frequency in descending order
        sorted_chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        
        # Construct the sorted string
        return ''.join(char * freq[char] for char in sorted_chars)
