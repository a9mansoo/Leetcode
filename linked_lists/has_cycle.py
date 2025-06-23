from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    fast = slow = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False


node_1 = ListNode("1")
node_2 = ListNode("2")
node_3 = ListNode("3")
node_4 = ListNode("4")

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_2

hasCycle(node_1)