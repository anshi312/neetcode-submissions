# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n < 1 or head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # count length N
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        prev = dummy
        for _ in range(length - n):
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next