class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left = []
        max_right = []
        
        maxi = float('-inf')
        for price in reversed(prices):
            maxi = max(price, maxi)
            max_right.append(maxi)
        
        mini = float('inf')
        for price in prices:
            mini = min(price, mini)
            min_left.append(mini)

        print(min_left)
        max_right.reverse()
        print(max_right)

        result = []
        for i in range(len(min_left)):
            diff = abs(min_left[i] - max_right[i])
            result.append(diff)
        
        return max(result)