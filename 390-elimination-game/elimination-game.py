class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        left_to_right = True
        head = 1
        step = 1

        while n > 1:
            if left_to_right or n % 2 == 1:
                head += step  # Move head forward when removing elements
            
            n //= 2  # Reduce the number of elements
            step *= 2  # Step doubles every round
            left_to_right = not left_to_right  # Toggle direction
        
        return head
        