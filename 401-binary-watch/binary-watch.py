class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []
        for h in range(12):  # Hours (0 to 11)
            for m in range(60):  # Minutes (0 to 59)
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    result.append("{}:{:02d}".format(h, m))  # Use .format() instead of f-strings
        return result

# Test Cases
solution = Solution()
print(solution.readBinaryWatch(1))  # Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
print(solution.readBinaryWatch(9))  # Output: []
