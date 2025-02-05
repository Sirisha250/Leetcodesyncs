class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1  # Start from the last digits

        while i >= 0 or j >= 0 or carry:
            sum_ = carry
            if i >= 0:
                sum_ += int(a[i])  # Convert char to int
                i -= 1
            if j >= 0:
                sum_ += int(b[j])
                j -= 1

            result.append(str(sum_ % 2))  # Append the remainder (0 or 1)
            carry = sum_ // 2  # Compute new carry

        return ''.join(result[::-1])  # Reverse and join to get final result

# Example usage:
sol = Solution()
print(sol.addBinary("11", "1"))      # Output: "100"
print(sol.addBinary("1010", "1011")) # Output: "10101"
