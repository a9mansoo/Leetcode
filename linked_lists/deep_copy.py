from typing import Optional




# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    """
    Original: A → B → C
    Becomes:  A → a → B → b → C → c
    """
    curr_node = head
    prev = None

    while curr_node != None:
        new_node = Node(curr_node.val, curr_node.next)
        prev = curr_node
        curr_node = curr_node.next
        prev.next = new_node
    
    curr_node = head
    p2_head = curr_node.next
    while curr_node != None:
        new_list_node = curr_node.next
        if new_list_node:
            new_list_node.random = curr_node.random
        if curr_node.next:
            next_node = curr_node.next.next 
            curr_node.next = next_node
            curr_node = next_node
        if new_list_node.next:
            new_list_node.next = new_list_node.next.next
    return p2_head


        




node_1 = Node(7)
node_2 = Node(13)
node_3  = Node(11)
node_4 = Node(10)
node_5 = Node(1)

node_1.next = node_2
node_1.random = None
node_2.next = node_3
node_2.random = node_1
node_3.next = node_4
node_4.next = node_5
node_5.next = None
node_3.random = node_5
node_4.random = node_3
node_5.random = node_1

p2 = copyRandomList(node_1)

curr_node = node_1
while curr_node is not None:
    print("-------------------------------------")
    print(f"Random: {getattr(curr_node.random, 'val', None)}")
    print(f"Value: {getattr(curr_node, 'val', None)}")
    print(f"Next: {getattr(curr_node, 'next', None)}")
    print("--------------------------------------")
    curr_node = curr_node.next

while p2 is not None:
    print("COPY")
    print(getattr(p2.random, 'val', None))
    print(getattr(p2, 'val', None))
    print(getattr(p2, 'next', None))
    p2 = p2.next