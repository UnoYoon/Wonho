# 연결리스트를 단순 반대로 뒤집어서 출력

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            next, curr.next = curr.next, prev
            prev, curr = curr, next
        return prev

# curr 1 -> 2 -> 3 -> 4 -> 5
# prev None

# curr 2 -> 3 -> 4 -> 5
# prev 1 -> None

# curr 3 -> 4 -> 5
# prev 2 -> 1 -> None

