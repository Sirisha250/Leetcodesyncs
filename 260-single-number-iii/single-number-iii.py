class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_all = 0
        for num in nums:
            xor_all ^= num  # XOR all numbers together
        
        # Get the rightmost set bit (where the two unique numbers differ)
        diff_bit = xor_all & -xor_all  

        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num  # XOR numbers in one group
            else:
                num2 ^= num  # XOR numbers in the other group
        
        return [num1, num2]
