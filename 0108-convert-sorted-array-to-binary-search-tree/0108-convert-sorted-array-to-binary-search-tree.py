# 왼쪽 서브 트리에는 부모보다 작은 값 (자식) 오른쪽 서브 트리에는 부모보다 큰 값(자식)
# 원래 트리에서 반대로 모양도 바꿔야한다. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node
        return helper(0, len(nums) - 1)