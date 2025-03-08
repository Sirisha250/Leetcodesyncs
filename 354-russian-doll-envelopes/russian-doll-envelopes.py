from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        # Sort by width ASCENDING, height DESCENDING (for same width)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Extract heights
        heights = [h for _, h in envelopes]

        # Apply LIS on heights
        lis = []
        for h in heights:
            idx = bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h

        return len(lis)
