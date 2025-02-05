class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []  # Final justified lines
        line = []  # Current line of words
        line_len = 0  # Length of words in line (excluding spaces)

        for word in words:
            if line and line_len + len(word) + len(line) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - line_len):
                    line[i % (len(line) - 1 or 1)] += ' '  # Distribute extra spaces
                
                res.append(''.join(line))  # Join line and store in result
                line, line_len = [], 0  # Reset for the next line
            
            line.append(word)
            line_len += len(word)

        # Left-justify the last line
        res.append(' '.join(line).ljust(maxWidth))

        return res

# Example usage:
sol = Solution()
print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(sol.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
  