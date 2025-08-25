from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        coords = [(r, c) for r in range(m) for c in range(n)]

        def key(rc):
            r, c = rc
            s = r + c
            # even sum -> prefer col; odd sum -> prefer row
            return (s, c) if s % 2 == 0 else (s, r)

        coords.sort(key=key)
        return [mat[r][c] for r, c in coords]
