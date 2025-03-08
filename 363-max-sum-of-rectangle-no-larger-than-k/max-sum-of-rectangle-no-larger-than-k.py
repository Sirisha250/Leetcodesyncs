from sortedcontainers import SortedList

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        max_sum = float('-inf')

        # Iterate over column pairs (left, right)
        for left in range(cols):
            row_sums = [0] * rows  # 1D array to store row sums
            
            for right in range(left, cols):
                # Update row_sums for the new right boundary
                for i in range(rows):
                    row_sums[i] += matrix[i][right]
                
                # Use SortedList to find the max subarray sum no larger than k
                prefix_sums = SortedList([0])
                curr_sum, local_max = 0, float('-inf')

                for sum_val in row_sums:
                    curr_sum += sum_val
                    # Binary search for the smallest prefix sum ≥ (curr_sum - k)
                    idx = prefix_sums.bisect_left(curr_sum - k)
                    if idx < len(prefix_sums):
                        local_max = max(local_max, curr_sum - prefix_sums[idx])
                    prefix_sums.add(curr_sum)

                max_sum = max(max_sum, local_max)
        
        return max_sum

# Example usage:
obj = Solution()
print(obj.maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))  # Output: 2
print(obj.maxSumSubmatrix([[2,2,-1]], 3))  # Output: 3
