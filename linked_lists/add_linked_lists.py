from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_l1 = l1
        head_l2 = l2

        carry = 0
        prev = None
        head = None
        while head_l1 != None or head_l2 != None or carry != 0:
            v1 = 0 if head_l1 is None else head_l1.val
            v2 = 0 if head_l2 is None else head_l2.val
            total = v1 + v2 + carry
            digit = total % 10
            carry = total // 10
            node = ListNode(digit)
            if prev:
                 prev.next = node
            else:
                 head = node
            prev = node
            if head_l1:
                head_l1 = head_l1.next
            if head_l2:
                head_l2 = head_l2.next
        return head


     
