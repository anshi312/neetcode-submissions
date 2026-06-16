# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return []

        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next

        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left].next = arr[right]
            left += 1
            arr[right].next = arr[left]
            right -= 1
        arr[left].next = None    
