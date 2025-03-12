class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)  # Handle multi-digit numbers
            elif char == '[':
                stack.append((current_str, current_num))  # Push previous state to stack
                current_str, current_num = "", 0  # Reset for inner part
            elif char == ']':
                last_str, num = stack.pop()  # Retrieve previous state
                current_str = last_str + num * current_str  # Decode substring
            else:
                current_str += char  # Append normal characters

        return current_str

# Test Cases
solution = Solution()
print(solution.decodeString("3[a]2[bc]"))  # "aaabcbc"
print(solution.decodeString("3[a2[c]]"))  # "accaccacc"
print(solution.decodeString("2[abc]3[cd]ef"))  # "abcabccdcdcdef"
