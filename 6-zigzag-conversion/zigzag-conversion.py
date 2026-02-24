class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s  

        res = [""] * numRows  # Initialize rows as empty strings

        for i, char in enumerate(s):
            pos = i % (2 * numRows - 2)  # Position in the zigzag cycle
            row = pos if pos < numRows else 2 * numRows - 2 - pos  # Map to correct row
            res[row] += char  # Append character to the correct row

        return "".join(res)  # Combine all rows into the final output