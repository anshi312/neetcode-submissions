"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = defaultdict(lambda: Node(0))
        dummy[None] = None

        curr = head
        while curr:
            dummy[curr].val = curr.val
            dummy[curr].next = dummy[curr.next]
            dummy[curr].random = dummy[curr.random]

            curr = curr.next
        return dummy[head]