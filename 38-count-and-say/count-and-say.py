class Solution:
    def countAndSay(self, n):
        # Start with the base case
        result = "1"
        
        # Generate the sequence for each number up to n
        for _ in range(2, n + 1):
            current = ""
            count = 1
            # Iterate over the string and count the consecutive characters
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    current += str(count) + result[i - 1]
                    count = 1
            # Add the last group
            current += str(count) + result[-1]
            result = current  # Update result for the next iteration
        
        return result
