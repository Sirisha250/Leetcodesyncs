class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)

        # Try every possible first and second number
        for i in range(1, n):  # First number end at i
            for j in range(i + 1, n):  # Second number end at j
                
                num1, num2 = num[:i], num[i:j]
                
                # Avoid numbers with leading zeros (except single '0')
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue

                while j < n:
                    num3 = str(int(num1) + int(num2))  # Expected next number
                    
                    if not num.startswith(num3, j):  # Check if next number matches
                        break
                    
                    j += len(num3)  # Move forward
                    num1, num2 = num2, num3  # Update previous numbers
                    
                    if j == n:  # If we reached the end of the string, it's valid
                        return True
                    
        return False
