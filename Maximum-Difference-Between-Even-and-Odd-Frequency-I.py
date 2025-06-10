class Solution:
    def maxDifference(self, s: str) -> int:
        mp = {}
        for ch in s:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1
        
        odd_values = []
        even_values = []
        for freq in mp.values():
            if freq % 2 == 0:
                even_values.append(freq)
            else:
                odd_values.append(freq)

        max_odd_value = max(odd_values)
        max_even_value = max(even_values)
        min_odd_value = min(odd_values)
        min_even_value = min(even_values)

        diff1 = max_odd_value - min_even_value
        diff2 = max_even_value - min_odd_value
        return diff1 
