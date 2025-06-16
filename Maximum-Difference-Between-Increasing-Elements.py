class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini = nums[0]
        diff = 0
        for i in range(1, len(nums)):
            if nums[i] - mini > 0 and nums[i] - mini  > diff:
                print(f"{nums[i]} : {diff}")
                diff = nums[i] - mini
            if nums[i] < mini:
                mini = nums[i]
        return diff if diff else -1