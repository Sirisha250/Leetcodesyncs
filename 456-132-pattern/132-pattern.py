class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []  # This will store pairs (num, min_left)
        min_left = float('inf')  # Track the minimum value to the left
        
        for num in nums:
            while stack and num >= stack[-1][0]:  # Maintain decreasing order
                stack.pop()
            
            if stack and num > stack[-1][1]:  # Found 132 pattern
                return True
            
            stack.append((num, min_left))  # Store (num, min_left)
            min_left = min(min_left, num)  # Update min_left
        
        return False
