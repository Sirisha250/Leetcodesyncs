class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n  # Ensures wrap-around behavior

        for i in range(n):
            if nums[i] == 0:  # Already visited or part of an invalid cycle
                continue

            slow, fast = i, next_index(i)

            # Check movement direction (all positive or all negative)
            while nums[fast] * nums[i] > 0 and nums[next_index(fast)] * nums[i] > 0:
                if slow == fast:  # Cycle detected
                    if slow == next_index(slow):  # Single-element cycle
                        break
                    return True

                slow = next_index(slow)
                fast = next_index(next_index(fast))

            # Mark visited nodes to prevent rechecking
            val = nums[i]
            while nums[i] * val > 0:
                next_i = next_index(i)
                nums[i] = 0  # Mark as visited
                i = next_i

        return False

        