class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")  # Set for quick lookup
        s = list(s)  # Convert to list for mutability
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1  # Move left pointer forward if not a vowel
            while left < right and s[right] not in vowels:
                right -= 1  # Move right pointer backward if not a vowel
            
            s[left], s[right] = s[right], s[left]  # Swap vowels
            left += 1
            right -= 1
        
        return "".join(s)  # Convert list back to string
