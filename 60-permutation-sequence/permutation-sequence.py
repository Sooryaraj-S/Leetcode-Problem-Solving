class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial

        # Initialize numbers
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert to 0-based index
        result = []

        # Build permutation step by step
        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            result.append(nums[index])
            nums.pop(index)
            k %= fact

        return "".join(result)