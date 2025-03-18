class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]  # Greed factor of children
        :type s: List[int]  # Cookie sizes
        :rtype: int
        """
        g.sort()  # Sort children by greed factor
        s.sort()  # Sort cookies by size
        
        child_i = 0  # Pointer for children
        cookie_i = 0  # Pointer for cookies
        
        while child_i < len(g) and cookie_i < len(s):
            if s[cookie_i] >= g[child_i]:  # Can the cookie satisfy the child?
                child_i += 1  # Move to the next child
            cookie_i += 1  # Move to the next cookie (used or too small)
        
        return child_i  # Number of satisfied children
