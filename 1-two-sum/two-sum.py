class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the number and its index
        num_to_index = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                # Return the indices of the two numbers
                return [num_to_index[complement], i]
            
            # Store the current number with its index in the dictionary
            num_to_index[num] = i

        