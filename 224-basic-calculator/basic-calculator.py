class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = 1  # 1 for '+', -1 for '-'
        result = 0  # Final evaluated result
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Form multi-digit number
            elif char in ["+", "-"]:
                result += sign * num  # Apply previous number
                num = 0  # Reset number
                sign = 1 if char == "+" else -1  # Update sign
            elif char == "(":
                stack.append(result)  # Save current result
                stack.append(sign)  # Save current sign
                result = 0  # Reset result for inner parentheses
                sign = 1  # Reset sign
            elif char == ")":
                result += sign * num  # Apply last number
                num = 0  # Reset number
                result *= stack.pop()  # Multiply with previous sign
                result += stack.pop()  # Add to previous result
        
        return result + (sign * num)  # Apply last pending number
