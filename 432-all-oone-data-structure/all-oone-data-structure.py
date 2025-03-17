from collections import defaultdict, OrderedDict

class AllOne(object):

    def __init__(self):
        self.key_count = defaultdict(int)  # Stores the frequency of keys
        self.freq_map = OrderedDict()  # Maps frequency to an ordered set of keys

    def _remove_key(self, key, freq):
        """Removes a key from the freq_map."""
        if freq in self.freq_map:
            self.freq_map[freq].discard(key)
            if not self.freq_map[freq]:
                del self.freq_map[freq]

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        freq = self.key_count[key]
        self.key_count[key] += 1
        
        self._remove_key(key, freq)
        self.freq_map.setdefault(freq + 1, set()).add(key)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key in self.key_count:
            freq = self.key_count[key]
            
            if freq == 1:
                del self.key_count[key]
            else:
                self.key_count[key] -= 1
            
            self._remove_key(key, freq)
            if freq > 1:
                self.freq_map.setdefault(freq - 1, set()).add(key)

    def getMaxKey(self):
        """
        :rtype: str
        """
        if not self.freq_map:
            return ""
        max_freq = max(self.freq_map)
        return next(iter(self.freq_map[max_freq]))

    def getMinKey(self):
        """
        :rtype: str
        """
        if not self.freq_map:
            return ""
        min_freq = min(self.freq_map)
        return next(iter(self.freq_map[min_freq]))
