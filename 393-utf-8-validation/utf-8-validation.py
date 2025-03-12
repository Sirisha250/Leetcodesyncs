class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0  # Number of continuation bytes expected

        for num in data:
            binary = format(num, '#010b')[-8:]  # Convert to binary and take last 8 bits

            if count == 0:  # If expecting a new character
                if binary.startswith('0'):  # 1-byte character (0xxxxxxx)
                    continue
                elif binary.startswith('110'):  # 2-byte character (110xxxxx 10xxxxxx)
                    count = 1
                elif binary.startswith('1110'):  # 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
                    count = 2
                elif binary.startswith('11110'):  # 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
                    count = 3
                else:
                    return False  # Invalid leading byte
            else:
                if not binary.startswith('10'):  # Check if continuation byte starts with '10'
                    return False
                count -= 1  # Reduce continuation count

        return count == 0  # Ensure no incomplete sequences

# Test Cases
solution = Solution()
print(solution.validUtf8([197, 130, 1]))  # True
print(solution.validUtf8([235, 140, 4]))  # False
