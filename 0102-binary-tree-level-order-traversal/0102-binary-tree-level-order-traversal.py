# 각 트리의 level 마다 리스트 안에 리스트로 값 출력 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        nodes_by_level = []
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()

            if len(nodes_by_level) <= level:
                nodes_by_level.append([])

            nodes_by_level[level].append(node.val)
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            
        return nodes_by_level