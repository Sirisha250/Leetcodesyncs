class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False  # Different lengths, cannot be a bijection
        
        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False  # Mismatch in mapping
            else:
                if word in word_to_char:
                    return False  # Word already mapped to a different character
                char_to_word[char] = word
                word_to_char[word] = char

        return True

        