from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)  # Use a dictionary to group anagrams
        
        for s in strs:
            sorted_str = ''.join(sorted(s))  # Sort the string to use as a key
            anagrams[sorted_str].append(s)  # Group the anagram under the sorted key
        
        return list(anagrams.values())  # Return the grouped anagrams as a list

# Example usage:
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

print(solution.groupAnagrams([""]))
# Output: [[""]]

print(solution.groupAnagrams(["a"]))
# Output: [["a"]]

        