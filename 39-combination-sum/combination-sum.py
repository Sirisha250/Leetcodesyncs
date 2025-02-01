class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, target, path):
            if target == 0:  # Found a valid combination
                result.append(list(path))
                return
            if target < 0:  # Exceeded the target
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)  # Allow repeated use of the same candidate
                path.pop()  # Backtrack
        
        backtrack(0, target, [])
        return result
