from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1.0 / value  # Reciprocal value

        # Step 2: DFS to evaluate queries
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0  # One of the nodes doesn't exist

            if start == end:
                return 1.0  # Division by itself

            visited.add(start)
            for neighbor, value in graph[start].items():
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return result * value
            return -1.0  # No path found
        
        # Step 3: Process each query
        results = []
        for num, den in queries:
            results.append(dfs(num, den, set()))
        return results

# Test Cases
solution = Solution()
print(solution.calcEquation(
    [["a", "b"], ["b", "c"]], 
    [2.0, 3.0], 
    [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
))  # Output: [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]

print(solution.calcEquation(
    [["a", "b"], ["b", "c"], ["bc", "cd"]], 
    [1.5, 2.5, 5.0], 
    [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
))  # Output: [3.75000, 0.40000, 5.00000, 0.20000]

print(solution.calcEquation(
    [["a", "b"]], 
    [0.5], 
    [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
))  # Output: [0.50000, 2.00000, -1.00000, -1.00000]
