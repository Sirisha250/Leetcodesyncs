class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_length = 0
        path_length = {0: 0}  # Dictionary to store cumulative path length at each depth
        
        for line in input.split("\n"):
            depth = line.count("\t")  # Determine depth based on tab count
            name = line.lstrip("\t")  # Remove leading tabs to get actual name
            
            if '.' in name:  # If it's a file
                max_length = max(max_length, path_length[depth] + len(name))
            else:  # If it's a directory
                path_length[depth + 1] = path_length[depth] + len(name) + 1  # +1 for '/'
        
        return max_length

        