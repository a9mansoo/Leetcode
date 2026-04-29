class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_dups(head):
    seen = set()
    current = head
    prev = None
    while current:
        if current.value in seen:
            prev.next = current.next
            current = current.next
        else:
            seen.add(current.value)
            prev = current
            current = current.next
    return head


def remove_dups_no_buffer(head):
    current = head
    while current:
        next_node = current.next
        prev = current
        while next_node:
            if next_node.value == current.value:
                prev.next = next_node.next
            else:
                prev = next_node
            next_node = next_node.next
        current = current.next
    return head


head = Node(1)

node_2 = Node(2)
head.next = node_2
node_3 = Node(2)
node_2.next = node_3
node_4 = Node(2)
node_3.next = node_4
node_5 = Node(4)
node_4.next = node_5
remove_dups_no_buffer(head)

while head:
    print(head.value)
    head = head.next