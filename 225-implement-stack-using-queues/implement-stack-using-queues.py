from collections import deque

class MyStack(object):

    def __init__(self):
        """Initialize the stack using a queue."""
        self.queue = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)  # Push element to the queue
        # Rotate the queue to maintain stack order
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns it.
        :rtype: int
        """
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0
