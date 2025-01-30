from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                # If the word is in the words list
                if word in word_count:
                    current_count[word] += 1

                    # If we have more occurrences of the word than needed
                    while current_count[word] > word_count[word]:
                        current_count[s[left:left + word_len]] -= 1
                        left += word_len

                    # If the window size matches the total length, it's a valid substring
                    if right - left == total_len:
                        result.append(left)
                else:
                    # Reset the window if the word is not in words
                    current_count.clear()
                    left = right

        return result
