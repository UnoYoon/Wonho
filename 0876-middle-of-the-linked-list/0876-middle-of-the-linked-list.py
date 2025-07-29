# 연결리스트의 중간 값을 구한 후 이후 연결되어있는 모든 노드들을 출력
# 중간값의 경우는 2가지 -> 2개(두 번째 중간 값으로 결정) or 1개(이 때는 신경 x)
# 1. 중간값 구하기
# 2. 조건1. 한개면 그냥 그 이후 연결리스트 출력
# 3. 조건2. 2개면 2번째걸로 결정 후 연결리스트 똑같이 출력


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_middle(node):
            if not node:
                return None
            slow = node
            fast = node

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        return find_middle(head)