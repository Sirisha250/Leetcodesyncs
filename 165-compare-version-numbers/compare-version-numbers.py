class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        # Pad shorter version with zeros
        length = max(len(v1), len(v2))
        v1 += [0] * (length - len(v1))
        v2 += [0] * (length - len(v2))

        # Compare each section
        for i in range(length):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        return 0
