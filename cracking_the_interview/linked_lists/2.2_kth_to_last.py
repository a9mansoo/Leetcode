class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def naive_approach(head, k):
    if not head:
        return None
    
    n = 0
    current = head
    while current:
        n+= 1
        current = current.next
    
    if k > n:
        return None
    
    index = n - k
    current = head
    i = 0
    while current:
        if index == i:
            return current
        i += 1
        current = current.next
    return None


def two_pointer_approach(head, k):
    if not head:
        return None
    
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    return slow

head = Node(1)
node_2 = Node(2)
head.next = node_2
node_3 = Node(3)
node_2.next = node_3
node_4 = Node(4)
node_3.next = node_4
node_5 = Node(5)
node_4.next = node_5
print(naive_approach(head, 2).value)

print(two_pointer_approach(head, 2).value)