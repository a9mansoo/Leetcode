import math


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def sol_1(head):
    current = head
    n = 0
    while current:
        n += 1
        current = current.next
    
    half_way = math.ceil(n / 2)
    current = head
    i = 0
    while current:
        i+= 1
        if i == half_way:
            return current.value
        current = current.next
    return None


def sol_2(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value if slow else None


        
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
print(sol_1(head))  # Output: 4
print(sol_2(head))  # Output: 4