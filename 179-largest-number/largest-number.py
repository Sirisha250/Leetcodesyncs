class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key

        def compare(a, b):
            # Compare based on the concatenation of strings
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0   # a and b are equal in this context

        # Convert all numbers to strings
        nums = list(map(str, nums))
        # Sort the numbers using the custom comparator
        nums.sort(key=cmp_to_key(compare))

        # Join the sorted numbers to form the largest number
        result = "".join(nums)
        # Handle the edge case where the result is "0"
        return result if result[0] != "0" else "0"


        