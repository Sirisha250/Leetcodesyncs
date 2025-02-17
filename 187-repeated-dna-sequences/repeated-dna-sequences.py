class Solution:
    def findRepeatedDnaSequences(self, s):
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            if substring in seen:
                repeated.add(substring)
            else:
                seen.add(substring)

        return list(repeated)

# Test the function
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
solution = Solution()
print(solution.findRepeatedDnaSequences(s))

