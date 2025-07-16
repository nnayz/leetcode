from collections import defaultdict
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odds = []
        evens = []
        alter_parity = []
        pt = 0 if nums[0] % 2 else 1# 0 means even, 1 means odd for tracking alternating parity
        for num in nums:
            if num % 2:
                odds.append(num)
                if pt == 0:
                    alter_parity.append(num)
                pt = 1
            else:
                evens.append(num)
                if pt == 1:
                    alter_parity.append(num)
                pt = 0

        return max(len(odds), len(evens), len(alter_parity))
