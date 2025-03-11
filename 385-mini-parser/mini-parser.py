class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):  # If s is a single integer
            return NestedInteger(int(s))
        
        stack = []
        num = ''
        for char in s:
            if char.isdigit() or char == '-':  # Build the number
                num += char
            elif char == '[':  # Start a new NestedInteger list
                stack.append(NestedInteger())
            elif char == ',' or char == ']':  # End of number or list
                if num:
                    stack[-1].add(NestedInteger(int(num)))  # Add integer to last list
                    num = ''
                if char == ']' and len(stack) > 1:  # If nested list ends, pop and add to previous list
                    last = stack.pop()
                    stack[-1].add(last)
        
        return stack[0]  # Root NestedInteger
