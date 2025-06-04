class Solution:
    def answerString(self, word: str, n: int) -> str:
        m = len(word) - n + 1 # Splits to be done with m length
        if n == 1:
            return word
        # else check all m length split and find max in them
        return max(word[i : i + m] for i in range(len(word)))
