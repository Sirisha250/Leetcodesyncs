class Solution:
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_steps(curr, n):
            steps = 0
            first, last = curr, curr + 1
            while first <= n:
                steps += min(last, n + 1) - first
                first *= 10
                last *= 10
            return steps
        
        curr = 1
        k -= 1
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        
        return curr