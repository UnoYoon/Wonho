# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 이 문제의 핵심은 루트 값보다 작으면 왼쪽, 루트 값보다 크면 오른쪽 둘 다 만족할 때 그 때 lca를 만족하는 조상 노드를 구할 수 있다. 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root 