class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start, len(s)):
                if is_palindrome(s[start:end+1]):
                    backtrack(end+1, path + [s[start:end+1]])

        result = []
        backtrack(0, [])
        return result
