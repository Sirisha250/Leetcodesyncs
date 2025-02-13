class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(a // b if a * b > 0 else -(-a // b))  # Correct integer division
                
            else:
                stack.append(int(token))  # Convert string to integer and push

        return stack[0]

# Test Cases
solution = Solution()

print(solution.evalRPN(["2","1","+","3","*"]))  # Output: 9
print(solution.evalRPN(["4","13","5","/","+"]))  # Output: 6
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # Output: 22
