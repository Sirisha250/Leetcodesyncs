from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Build adjacency list and in-degree array
        adj_list = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
        
        # Step 2: Initialize queue with courses having 0 in-degree
        queue = deque([course for course in in_degree if in_degree[course] == 0])
        order = []
        
        # Step 3: Process courses using BFS
        while queue:
            course = queue.popleft()
            order.append(course)
            
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check if all courses are in order (cycle detection)
        return order if len(order) == numCourses else []
