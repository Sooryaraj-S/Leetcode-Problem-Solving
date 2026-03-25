class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()   # sort to handle duplicates
        result, path = [], []
        n = len(nums)

        def dfs(start):
            result.append(path[:])   # every path is a subset
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue   # skip duplicate at same depth
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return result