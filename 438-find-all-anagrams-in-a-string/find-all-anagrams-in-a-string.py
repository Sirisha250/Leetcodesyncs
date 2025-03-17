from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        
        p_count = Counter(p)
        s_count = Counter(s[:len(p) - 1])
        result = []
        
        for i in range(len(p) - 1, len(s)):
            s_count[s[i]] += 1
            if s_count == p_count:
                result.append(i - len(p) + 1)
            
            s_count[s[i - len(p) + 1]] -= 1
            if s_count[s[i - len(p) + 1]] == 0:
                del s_count[s[i - len(p) + 1]]
        
        return result
