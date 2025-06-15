class Solution:
    def nextRow(self, n: List[int]) -> List[int]:
        if len(n) == 1:
            return [1, 1]
        result = [1] * (len(n) + 1)
        for i in range(1, len(result) - 1):
            result[i] = n[i - 1] + n[i]
        return result

    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        initial_row = [1]
        for i in range(numRows - 1):
            next_row = self.nextRow(initial_row)
            result.append(next_row)
            initial_row = next_row
        return result