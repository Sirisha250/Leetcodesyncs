class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                # Get the top element of the stack (or a dummy value if the stack is empty)
                top_element = stack.pop() if stack else '#'
                # Check if the mapping for the current character matches the top of the stack
                if mapping[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched
        return not stack

        