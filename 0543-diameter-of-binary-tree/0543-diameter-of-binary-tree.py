# 가장 큰 지름을 가진 바이너리 트리 구하기
# root를 지날 수도 안 지날 수도 있다.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)

            self.diameter = max(self.diameter, left_height + right_height)
            
            return 1 + max(left_height, right_height)

        height(root)

        return self.diameter