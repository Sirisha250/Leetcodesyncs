class Solution:
    def maxProduct(self, words):
        bitmasks = {}
        max_product = 0

        # Step 1: Create a bitmask for each word
        for word in words:
            mask = 0
            for char in word:
                mask |= (1 << (ord(char) - ord('a')))  # Set bit for character
            
            # Store the max length for each unique bitmask
            bitmasks[mask] = max(bitmasks.get(mask, 0), len(word))
        
        # Step 2: Compare bitmasks
        for mask1 in bitmasks:
            for mask2 in bitmasks:
                if mask1 & mask2 == 0:  # No common letters
                    max_product = max(max_product, bitmasks[mask1] * bitmasks[mask2])
        
        return max_product

# Example test cases
sol = Solution()
print(sol.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))  # Output: 16
print(sol.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))     # Output: 4
print(sol.maxProduct(["a","aa","aaa","aaaa"]))                    # Output: 0
