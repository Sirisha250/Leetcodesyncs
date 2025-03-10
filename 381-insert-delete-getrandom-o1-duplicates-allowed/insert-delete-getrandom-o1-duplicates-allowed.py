import random

class RandomizedCollection(object):

    def __init__(self):
        """ Initialize the data structure. """
        self.val_to_indices = {}  # Maps value to set of indices
        self.values = []  # Stores elements for getRandom()

    def insert(self, val):
        """ Inserts a value. Returns True if first insertion, False if already exists. """
        first_insert = val not in self.val_to_indices
        if first_insert:
            self.val_to_indices[val] = set()
        
        self.val_to_indices[val].add(len(self.values))
        self.values.append(val)
        return first_insert

    def remove(self, val):
        """ Removes a value. Returns True if removed, False if not found. """
        if val not in self.val_to_indices or not self.val_to_indices[val]:
            return False
        
        # Get index of the value to remove
        remove_idx = self.val_to_indices[val].pop()
        last_val = self.values[-1]

        if remove_idx < len(self.values) - 1:  # If not removing last element
            # Swap with last element
            self.values[remove_idx] = last_val
            self.val_to_indices[last_val].add(remove_idx)
            self.val_to_indices[last_val].remove(len(self.values) - 1)

        # Remove last element
        self.values.pop()
        if not self.val_to_indices[val]:  # Clean up empty sets
            del self.val_to_indices[val]
        
        return True

    def getRandom(self):
        """ Returns a random element. """
        return random.choice(self.values)
