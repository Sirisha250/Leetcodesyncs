class NestedIterator:
    def __init__(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.flatten(nestedList)

    def flatten(self, nestedList):
        # Add elements to stack in **reverse order** for correct processing
        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():  # If it's an integer, we are ready
                return True
            self.stack.pop()  # Remove list
            self.flatten(top.getList())  # Unpack list elements onto stack
        return False
