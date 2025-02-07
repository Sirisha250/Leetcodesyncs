class Solution(object):
    def __init__(self):
        self.memo = {}  # Memoization dictionary

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):  # Pruning: if character counts don't match, return False
            return False
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]

        n = len(s1)
        for i in range(1, n):  # Try all possible partitions
            # Case 1: Without swapping
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.memo[(s1, s2)] = True
                return True
            # Case 2: With swapping
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                self.memo[(s1, s2)] = True
                return True

        self.memo[(s1, s2)] = False
        return False
