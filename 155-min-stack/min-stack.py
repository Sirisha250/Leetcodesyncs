class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        
        # Push onto min_stack if it's the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])  # Maintain the last min value

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1] if self.min_stack else None
