class Solution(object):
    def minWindow(self, s, t):
        """
        This function finds the minimum window substring of `s` that contains all the characters of `t` (including duplicates).
        If no such window exists, returns an empty string.
        
        :type s: str
        :type t: str
        :rtype: str
        """

        # Early return if either string is empty or t is longer than s
        if not t or not s or len(t) > len(s):
            return ''

        # Count the frequency of characters in t
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        # The total number of unique characters in t that need to be present in the window
        required = len(t_count)

        # Counter to keep track of when we have a valid window
        formed = 0

        # Dictionary to keep a count of all the unique characters in the current window
        sub_s_count = {}

        start = 0  # Left pointer of the window
        min_len = float('inf')  # Length of the smallest window found
        min_window_start = 0  # Start index of the smallest window found

        # Iterate over s using `end` as the right pointer of the window
        for end in range(len(s)):
            sub_s_count[s[end]] = sub_s_count.get(s[end], 0) + 1

            # Check if the current window contains the required characters with correct frequency
            if s[end] in t_count and sub_s_count[s[end]] == t_count[s[end]]:
                formed += 1

            # Try to contract the window from the left as long as the window is valid
            while start <= end and formed == required:
                char = s[start]  # Character at the left pointer

                # Update the minimum window
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    min_window_start = start

                # Prepare to move the left pointer by reducing the frequency of the current character
                sub_s_count[char] -= 1

                # Check if the window is still valid after moving the left pointer
                if char in t_count and sub_s_count[char] < t_count[char]:
                    formed -= 1
                start += 1

        # Return the minimum window or an empty string if no valid window was found
        return "" if min_len == float('inf') else s[min_window_start:min_window_start + min_len]