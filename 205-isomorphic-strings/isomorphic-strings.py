class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False  # Different lengths can't be isomorphic

        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False  # Conflict in mapping s -> t
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False  # Conflict in mapping t -> s

            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True
