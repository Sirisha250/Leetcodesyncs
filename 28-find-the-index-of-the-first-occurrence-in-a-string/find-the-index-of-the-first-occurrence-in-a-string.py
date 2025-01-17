class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # If needle is empty, return 0 (as per problem statement)
        if not needle:
            return 0
        
        # Use the find() method to find the first occurrence of needle in haystack
        return haystack.find(needle)

# Create an instance of the Solution class
solution = Solution()

# Example 1:
haystack1 = "sadbutsad"
needle1 = "sad"
output1 = solution.strStr(haystack1, needle1)
print("Example 1 Output: {}".format(output1))  # Expected Output: 0

# Example 2:
haystack2 = "leetcode"
needle2 = "leeto"
output2 = solution.strStr(haystack2, needle2)
print("Example 2 Output: {}".format(output2))  # Expected Output: -1
