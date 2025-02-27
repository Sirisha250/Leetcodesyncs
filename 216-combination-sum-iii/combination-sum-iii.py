class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, path, target):
            if len(path) == k:
                if target == 0:
                    result.append(path[:])
                return
            
            for i in range(start, 10):  # Numbers from 1 to 9
                if i > target:
                    break  # Stop if the number is greater than the remaining sum
                path.append(i)
                backtrack(i + 1, path, target - i)
                path.pop()  # Backtrack
        
        backtrack(1, [], n)
        return result

# Example usage:
sol = Solution()
print(sol.combinationSum3(3, 7))  # [[1,2,4]]
print(sol.combinationSum3(3, 9))  # [[1,2,6],[1,3,5],[2,3,4]]
print(sol.combinationSum3(4, 1))  # []
