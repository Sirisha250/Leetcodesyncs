class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]  # Start with the first string as the prefix
        
        for s in strs[1:]:
            while not s.startswith(prefix):  # Trim prefix until it matches
                prefix = prefix[:-1]  # Remove last character
                if not prefix:
                    return ""  # No common prefix found
        
        return prefix

# Example usage:
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""

        