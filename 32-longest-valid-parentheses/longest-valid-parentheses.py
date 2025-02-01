class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Initialize stack with -1 to handle edge cases
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push index of '('
            else:  # char == ')'
                stack.pop()  # Try to match with last '('
                if not stack:
                    stack.append(i)  # Store the last unmatched ')'
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length
