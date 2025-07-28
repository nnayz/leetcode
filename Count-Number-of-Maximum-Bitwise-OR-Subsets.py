class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = 0

        for num in nums:
            max_or |= num

        def dfs(idx: int, cur_or: int) -> int:
            if cur_or == max_or:
                after = n - idx
                return 2**after

            if idx == n:
                return 0

            take = dfs(idx + 1, cur_or | nums[idx])
            skip = dfs(idx + 1, cur_or)

            return take + skip

        return dfs(0, 0)