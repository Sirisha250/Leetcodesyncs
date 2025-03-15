class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = 0
        mask = 0
        
        for i in range(31, -1, -1):  # Check bits from MSB to LSB
            mask |= (1 << i)  # Include the current bit in mask
            prefixes = set()  # HashSet to store prefixes
            
            # Store prefixes with only i most significant bits
            for num in nums:
                prefixes.add(num & mask)

            # Try to maximize the XOR
            candidate = max_xor | (1 << i)  # Assume we can set this bit
            
            for prefix in prefixes:
                if (candidate ^ prefix) in prefixes:
                    max_xor = candidate  # If possible, update max_xor
                    break  # No need to check further
            
        return max_xor
