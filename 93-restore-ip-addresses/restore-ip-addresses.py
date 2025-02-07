class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        
        def backtrack(start, path):
            if len(path) == 4:  # Must have exactly 4 octets
                if start == len(s):  # Entire string used
                    res.append(".".join(path))
                return
            
            for length in range(1, 4):  # Each octet can be 1-3 digits
                if start + length > len(s): 
                    break  # Out of bounds
                
                part = s[start:start+length]
                
                if (len(part) > 1 and part[0] == '0') or int(part) > 255:
                    continue  # Invalid segment
                
                backtrack(start + length, path + [part])  # Recur with next part
        
        backtrack(0, [])
        return res
