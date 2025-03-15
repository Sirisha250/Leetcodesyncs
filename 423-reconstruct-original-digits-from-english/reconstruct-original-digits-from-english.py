from collections import Counter

class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count occurrences of all characters
        count = Counter(s)
        output = [0] * 10  # To store occurrences of each digit

        # Unique identifiers for certain numbers
        output[0] = count['z']  # "zero"
        output[2] = count['w']  # "two"
        output[4] = count['u']  # "four"
        output[6] = count['x']  # "six"
        output[8] = count['g']  # "eight"

        # Non-unique but can be determined after unique ones are removed
        output[3] = count['h'] - output[8]  # "three" (eight also has 'h')
        output[5] = count['f'] - output[4]  # "five" (four also has 'f')
        output[7] = count['s'] - output[6]  # "seven" (six also has 's')

        # Finally, determine 1 and 9
        output[1] = count['o'] - output[0] - output[2] - output[4]  # "one" (zero, two, four share 'o')
        output[9] = count['i'] - output[5] - output[6] - output[8]  # "nine" (five, six, eight share 'i')

        # Construct the final result
        result = ''.join(str(i) * output[i] for i in range(10))
        return result
