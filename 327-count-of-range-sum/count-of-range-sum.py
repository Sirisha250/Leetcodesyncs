class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        def merge_sort(start, end):
            if start >= end:
                return 0
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)
            
            j = k = mid + 1
            for left in prefix_sums[start:mid+1]:
                while k <= end and prefix_sums[k] - left < lower:
                    k += 1
                while j <= end and prefix_sums[j] - left <= upper:
                    j += 1
                count += j - k
            
            # Merge step (sort the range to maintain order)
            prefix_sums[start:end+1] = sorted(prefix_sums[start:end+1])
            return count

        # Step 1: Compute prefix sums
        prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        # Step 2: Use merge sort to count valid range sums
        return merge_sort(0, len(prefix_sums) - 1)

# Test cases
sol = Solution()
print(sol.countRangeSum([-2,5,-1], -2, 2))  # Output: 3
print(sol.countRangeSum([0], 0, 0))        # Output: 1
