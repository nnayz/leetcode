# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_values = []  # Store values of nodes at the current level

            for _ in range(level_size):
                current_node = queue.popleft()
                level_values.append(current_node.val)  # Extract the value

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            if level_values:
                res.append(max(level_values))

        return res
            
        