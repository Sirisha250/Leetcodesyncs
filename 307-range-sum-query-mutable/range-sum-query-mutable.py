class NumArray:
    def __init__(self, nums):
        if not nums:
            return
        
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)

        # Build segment tree
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, val):
        # Update value at index
        pos = index + self.n
        self.tree[pos] = val

        # Update ancestors in segment tree
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]

    def sumRange(self, left, right):
        # Compute sum from left to right
        left += self.n
        right += self.n
        total = 0

        while left <= right:
            if left % 2 == 1:
                total += self.tree[left]
                left += 1
            if right % 2 == 0:
                total += self.tree[right]
                right -= 1

            left //= 2
            right //= 2
        
        return total

# Example usage
numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2))  # Output: 9
numArray.update(1, 2)           # nums = [1, 2, 5]
print(numArray.sumRange(0, 2))  # Output: 8
