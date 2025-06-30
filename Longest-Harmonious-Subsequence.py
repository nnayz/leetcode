class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mp = Counter(nums)
        max_length = 0
        for num in mp:
            if num + 1 in mp:
                current_length = mp[num] + mp[num + 1]
                max_length = max(max_length, current_length)

        return max_length