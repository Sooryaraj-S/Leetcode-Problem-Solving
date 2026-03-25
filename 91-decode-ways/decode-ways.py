class Solution:
    # Dynamic programming array to store intermediate results
    dp = []

    # Depth-first search helper function to count decoding ways
    def dfs(self, s, i):
        # If the index exceeds the string size, return 0 as it is invalid
        if i > len(s):
            return 0
        
        # If the index is at the end of the string, a valid way is found
        if i == len(s):
            return 1

        # If the result is already computed, return it to avoid recomputation
        if self.dp[i] != -1:
            return self.dp[i]

        # If the current character is '0', it cannot be decoded into any letter
        if s[i] == '0':
            return 0

        # Check if it's possible to decode one or two characters
        if s[i] == '1' or (i < len(s) - 1 and s[i] == '2' and '0' <= s[i + 1] <= '6'):
            self.dp[i] = self.dfs(s, i + 1) + self.dfs(s, i + 2)
        else:
            self.dp[i] = self.dfs(s, i + 1)

        return self.dp[i]

    # Main function to return the number of decoding ways
    def numDecodings(self, s):
        # Clear the dp array and resize it to match the size of the input string
        self.dp = [-1] * len(s)

        # Start the dfs from the beginning of the string
        return self.dfs(s, 0)