class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def get_distance(start):
            dist = [-1] * n
            current = start
            d = 0
            while current != -1 and dist[current] == -1:
                dist[current] = d
                current = edges[current]
                d += 1
            return dist
        dist1 = get_distance(node1)
        dist2 = get_distance(node2)

        min_dist = float('inf')
        result = -1

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i
        return result
