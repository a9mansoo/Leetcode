from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        left_node = None
        right_node = None
        curr_head = head
        right_dist = right - left
        left_parent = None

        while left > 1:
            left_parent = curr_head
            curr_head = curr_head.next
            left -= 1
        left_node = curr_head
        
        print (left_node.val)

        while (right_dist) > 0:
            curr_head = curr_head.next
            right_dist -= 1
        right_node = curr_head
        right_child = right_node.next


        prev_node = None
        curr_node = left_node
        while curr_node != right_child:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        # Reconnect
        if left_parent is not None:
            left_parent.next = right_node
        else:
            head = right_node

        left_node.next = right_child

        return head



list_node1 = ListNode(1)
list_node2 = ListNode(2)
list_node3 = ListNode(3)
list_node4= ListNode(4)
list_node5 = ListNode(5)

head = list_node1
list_node1.next = list_node2
# list_node1.next = list_node2
# list_node2.next = list_node3
# list_node3.next = list_node4
# list_node4.next = list_node5

sol = Solution()
# sol.reverseBetween(head, 2, 4)
# sol.reverseBetween(list_node5, 1, 1)
sol.reverseBetween(head, 1, 2)
