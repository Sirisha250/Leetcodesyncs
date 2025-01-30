class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()  # To store characters in the current window
        left = 0  # Left pointer of the window
        max_length = 0  # To keep track of the maximum length
        
        # Right pointer iterates through the string
        for right in range(len(s)):
            # If the character is already in the window, move the left pointer
            while s[right] in char_set:
                char_set.remove(s[left])  # Remove the left character
                left += 1  # Shrink the window from the left
            
            # Add the current character to the window
            char_set.add(s[right])
            
            # Update the maximum length of the substring
            max_length = max(max_length, right - left + 1)
        
        return max_length



# Test case
s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))  # Output: 3


