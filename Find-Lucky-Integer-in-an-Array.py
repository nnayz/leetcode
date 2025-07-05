class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = defaultdict(int)
        for num in arr:
            mp[num] += 1
        
        maxi = -1
        for key, value in mp.items():
            if key == value:
                maxi = max(maxi, key)
        
        return maxi