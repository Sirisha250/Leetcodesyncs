class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if not s1 or not s2:
            return 0
        
        index_map = {}  # Dictionary to detect cycles
        s1_count = s2_count = 0  # Counts of s1 and s2 processed
        index = 0  # Pointer for s2

        while s1_count < n1:
            for char in s1:
                if char == s2[index]:  # Match found
                    index += 1
                    if index == len(s2):  # One full s2 sequence found
                        s2_count += 1
                        index = 0
            
            s1_count += 1
            
            if index in index_map:  # Cycle detected
                prev_s1_count, prev_s2_count = index_map[index]
                cycle_length = s1_count - prev_s1_count
                cycle_s2_count = s2_count - prev_s2_count
                
                remaining_cycles = (n1 - s1_count) // cycle_length
                s1_count += remaining_cycles * cycle_length
                s2_count += remaining_cycles * cycle_s2_count
            
            index_map[index] = (s1_count, s2_count)

        return s2_count // n2
