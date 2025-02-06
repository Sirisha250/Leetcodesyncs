class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, path):
            # If the combination has k elements, add to the result
            if len(path) == k:
                result.append(path[:])  # Make a copy of path
                return
            
            # Iterate from 'start' to 'n' and generate combinations
            for i in range(start, n + 1):
                path.append(i)  # Include current number
                backtrack(i + 1, path)  # Recursive call for next numbers
                path.pop()  # Backtrack by removing the last number

        backtrack(1, [])
        return result

# Example test cases
solution = Solution()
print(solution.combine(4, 2))  # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(solution.combine(1, 1))  # Output: [[1]]

        