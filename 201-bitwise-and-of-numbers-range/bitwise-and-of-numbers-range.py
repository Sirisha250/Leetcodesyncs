class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Shift left and right until they become equal
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # After shifting, the common prefix is found in 'left'
        return left << shift

# Example 1:
left1, right1 = 5, 7
solution = Solution()
output1 = solution.rangeBitwiseAnd(left1, right1)
print("Example 1 Output: {}".format(output1))  # Expected Output: 4

# Example 2:
left2, right2 = 0, 0
output2 = solution.rangeBitwiseAnd(left2, right2)
print("Example 2 Output: {}".format(output2))  # Expected Output: 0

# Example 3:
left3, right3 = 1, 2147483647
output3 = solution.rangeBitwiseAnd(left3, right3)
print("Example 3 Output: {}".format(output3))  # Expected Output: 0


        