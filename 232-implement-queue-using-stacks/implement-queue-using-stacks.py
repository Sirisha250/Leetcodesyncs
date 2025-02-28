class MyQueue(object):

    def __init__(self):
        """Initialize two stacks."""
        self.s1 = []  # Main stack for push operations
        self.s2 = []  # Helper stack for pop/peek

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self._move_s1_to_s2()
        return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self._move_s1_to_s2()
        return self.s2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.s1 and not self.s2  # Both stacks should be empty

    def _move_s1_to_s2(self):
        """Helper function to transfer elements from s1 to s2 if s2 is empty."""
        if not self.s2:  # Move only if s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())

