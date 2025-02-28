class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        result = []
        start = nums[0]  # Start of current range
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:  # If not consecutive
                if start == nums[i - 1]:  
                    result.append(str(start))  # Single number range
                else:
                    result.append("{}->{}".format(start, nums[i - 1]))  # Python 2 compatible format
                
                start = nums[i]  # Start new range
        
        # Handle the last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append("{}->{}".format(start, nums[-1]))  # Python 2 compatible format
        
        return result

