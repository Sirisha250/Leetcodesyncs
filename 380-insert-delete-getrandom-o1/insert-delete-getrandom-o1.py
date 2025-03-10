import random

class RandomizedSet(object):

    def __init__(self):
        """ Initialize your data structure here. """
        self.val_to_idx = {}  # Maps value to index in list
        self.values = []  # Stores the actual values

    def insert(self, val):
        """ Inserts a value. Returns true if it was inserted, false if already exists. """
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """ Removes a value. Returns true if removed, false if not found. """
        if val not in self.val_to_idx:
            return False
        
        # Swap element with last element for O(1) deletion
        last_val = self.values[-1]
        idx = self.val_to_idx[val]
        
        # Move last element to idx position
        self.values[idx] = last_val
        self.val_to_idx[last_val] = idx

        # Remove last element
        self.values.pop()
        del self.val_to_idx[val]

        return True

    def getRandom(self):
        """ Returns a random element. """
        return random.choice(self.values)
