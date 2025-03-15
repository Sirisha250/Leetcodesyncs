class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:  # The first jump must be exactly 1 unit
            return False

        stone_positions = {stone: set() for stone in stones}
        stone_positions[0].add(0)  # The first stone starts with a jump size of 0

        for stone in stones:
            for jump in stone_positions[stone]:
                for next_jump in (jump - 1, jump, jump + 1):
                    if next_jump > 0 and (stone + next_jump) in stone_positions:
                        stone_positions[stone + next_jump].add(next_jump)

        return bool(stone_positions[stones[-1]])  # If last stone has any jumps, return True
