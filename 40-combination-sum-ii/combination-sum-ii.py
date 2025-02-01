class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, target, path):
            if target == 0:  # Found a valid combination
                result.append(list(path))  # Make a copy of the current path
                return
            if target < 0:  # Exceeded the target, no need to continue
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates: if the current number is the same as the previous one, skip it
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include candidates[i] in the path
                path.append(candidates[i])
                # Explore the next element with the reduced target (i+1 to avoid re-using the same element in the same combination)
                backtrack(i + 1, target - candidates[i], path)
                # Backtrack: remove the last element to try the next possible candidate
                path.pop()
        
        # Sort candidates to handle duplicates
        candidates.sort()
        # Start the backtracking
        backtrack(0, target, [])
        return result
