from collections import defaultdict, OrderedDict

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # {key: (value, frequency)}
        self.freq_table = defaultdict(OrderedDict)  # {frequency: OrderedDict(keys)}
        self.min_freq = 0  # Track the minimum frequency

    def _update_freq(self, key):
        """Helper function to update the frequency of a key."""
        value, freq = self.cache[key]
        
        # Remove key from current frequency list
        del self.freq_table[freq][key]
        if not self.freq_table[freq]:  # If empty, remove the frequency bucket
            del self.freq_table[freq]
            if self.min_freq == freq:
                self.min_freq += 1  # Update min frequency

        # Update frequency
        new_freq = freq + 1
        self.cache[key] = (value, new_freq)
        self.freq_table[new_freq][key] = None  # Maintain order
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self._update_freq(key)
        return self.cache[key][0]  # Return value only

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return

        if key in self.cache:
            # Update value and frequency
            self.cache[key] = (value, self.cache[key][1])
            self._update_freq(key)
            return
        
        # If cache is full, remove LFU element
        if len(self.cache) >= self.capacity:
            lfu_key, _ = self.freq_table[self.min_freq].popitem(last=False)  # Remove LRU from LFU
            del self.cache[lfu_key]  # Remove from main cache

        # Insert new key
        self.cache[key] = (value, 1)  # Set frequency to 1
        self.freq_table[1][key] = None  # Insert into frequency table
        self.min_freq = 1  # Reset min frequency to 1
