class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")  # Remove spaces
        stack = []
        num = 0
        sign = "+"  # The previous sign (default is '+')

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  # Build the number digit by digit
            
            if char in "+-*/" or i == len(s) - 1:  # Process when operator or end of string
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / float(num)))  # Truncate towards zero
                
                num = 0  # Reset num for the next number
                sign = char  # Update the sign
        
        return sum(stack)  # Sum up all numbers in the stack

        