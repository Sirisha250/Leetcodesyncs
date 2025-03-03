class Solution:
    def addOperators(self, num, target):
        res = []
        
        def dfs(index, path, curr_value, prev_value):
            # Base Case: If we processed all digits and got the target, add to result
            if index == len(num):
                if curr_value == target:
                    res.append(path)
                return
            
            # Try all possible substrings starting from `index`
            for i in range(index, len(num)):
                # Extract the number from `num[index:i+1]`
                sub_str = num[index:i+1]
                curr_num = int(sub_str)

                # Avoid numbers with leading zeros, e.g., "05" is invalid
                if len(sub_str) > 1 and sub_str[0] == '0':
                    break
                
                # Case 1: First number (no operator needed)
                if index == 0:
                    dfs(i + 1, sub_str, curr_num, curr_num)
                else:
                    # Case 2: Addition
                    dfs(i + 1, path + "+" + sub_str, curr_value + curr_num, curr_num)
                    
                    # Case 3: Subtraction
                    dfs(i + 1, path + "-" + sub_str, curr_value - curr_num, -curr_num)
                    
                    # Case 4: Multiplication (handle operator precedence)
                    new_value = (curr_value - prev_value) + (prev_value * curr_num)
                    dfs(i + 1, path + "*" + sub_str, new_value, prev_value * curr_num)
        
        # Start DFS
        dfs(0, "", 0, 0)
        return res
