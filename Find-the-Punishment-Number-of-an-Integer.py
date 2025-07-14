class Solution:
    def partition(self, x, target):
        if x == target: return True
        if x == 0: return target == 0
        for m in (10, 100, 1000):
            if self.partition(x // m, target-x % m):
                return True
        return False
    def punishmentNumber(self, n: int) -> int:
        return sum( x for i in range(1, n + 1) if self.partition(x:=i*i, i))
        