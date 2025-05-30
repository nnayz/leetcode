class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges) # Number of nodes [ 0 -> 2, 1 -> 2, 2 -> 3, 3 -> -1 ]
        dist1 = [-1] * n #. [ -1, -1, -1, -1 ]
        dist2 = [-1] * n #. [ -1, -1, -1, -1 ]

        current = node1 # 0
        d = 0 # Initialisation
        while current != -1 and dist1[current] == -1: # -1 represents a terminal
            dist1[current] = d
            current = edges[current]
            d += 1
        
        print(dist1)
        # For the node 2
        current = node2 # 1
        d = 0
        while current != -1 and dist2[current] == -1:
            dist2[current] = d
            current = edges[current]
            d += 1
        
        print(dist2)

        # Returning the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from the node2 to that node is minimised. 

        min_dist = float('inf')
        result = -1
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i
        return result


