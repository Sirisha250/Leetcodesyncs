class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize result array
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Multiply digit by digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_ = mul + result[i + j + 1]  # Add existing carry
                
                result[i + j + 1] = sum_ % 10  # Store unit place
                result[i + j] += sum_ // 10    # Carry to the next position

        # Convert result to string and remove leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')

        return result_str if result_str else "0"

# Example usage:
solution = Solution()
print(solution.multiply("2", "3"))       # Output: "6"
print(solution.multiply("123", "456"))   # Output: "56088"
