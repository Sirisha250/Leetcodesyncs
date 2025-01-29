class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))  # Add completed combination
                return
            
            for letter in phone_map[digits[index]]:
                backtrack(index + 1, path + [letter])  # Recurse with next digit
        
        backtrack(0, [])
        return result

# Example usage:
sol = Solution()
print(sol.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(sol.letterCombinations(""))    # Output: []
print(sol.letterCombinations("2"))   # Output: ["a","b","c"]
