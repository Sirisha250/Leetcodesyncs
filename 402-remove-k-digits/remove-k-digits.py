class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        
        for digit in num:
            # Remove larger digits to form a smaller number
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Remove remaining k digits from the end if necessary
        while k > 0 and stack:
            stack.pop()
            k -= 1
        
        # Convert stack to string & remove leading zeros
        result = "".join(stack).lstrip("0")
        
        # If result is empty, return "0"
        return result if result else "0"

# Test Cases
solution = Solution()
print(solution.removeKdigits("1432219", 3))  # Output: "1219"
print(solution.removeKdigits("10200", 1))    # Output: "200"
print(solution.removeKdigits("10", 2))       # Output: "0"
