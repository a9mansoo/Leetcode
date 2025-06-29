from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(-1)
    tail = head
    while list1 is not None and list2 is not None:
        if list2.val <= list1.val:
            tail.next = list2
            list2 = list2.next
        elif list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        tail = tail.next
    tail.next = list1 if list1 else list2

    return head.next


# l1 = [1, 3, 5]
# l2 = [2, 4, 6]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node3
node3.next = node5
l1 = node1

node2.next = node4
node4.next = node6
l2 = node2
mergeTwoLists(l1, l2)