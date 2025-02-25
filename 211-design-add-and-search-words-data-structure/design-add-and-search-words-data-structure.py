class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        Searches for a word in the data structure, allowing '.' as a wildcard.
        :type word: str
        :rtype: bool
        """
        return self._search_recursive(word, 0, self.root)

    def _search_recursive(self, word, index, node):
        """
        Helper function for searching with support for '.' wildcard.
        """
        if index == len(word):
            return node.is_end_of_word

        char = word[index]
        if char == '.':
            # Wildcard: Try all possible child nodes
            for child in node.children.values():
                if self._search_recursive(word, index + 1, child):
                    return True
        elif char in node.children:
            # Regular character: Move to next node
            return self._search_recursive(word, index + 1, node.children[char])

        return False
