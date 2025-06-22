class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        remaining_char = len(s) % k
        if not remaining_char == 0:
            for _ in range(k - remaining_char):
                s = s + fill
        
        print(s)

        result = []
        i, j = 0, k
        while j <= len(s):
            result.append(s[i:j])
            i += k
            j += k
        
        return result
