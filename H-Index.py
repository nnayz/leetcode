class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = len(citations)
        citations.sort()

        for i, v in enumerate(citations):
            if papers - i <= v:
                return papers - i
        return 0
        