class ListNode:

    def __init__(self, val=None, key=None, prev_node=None, next_node=None):
        self.val = val
        self.key = key
        self.prev_node = prev_node
        self.next_node = next_node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
    
    def _remove_node(self, node):
        prev_node = node.prev_node
        next_node = node.next_node
        prev_node.next_node = next_node
        next_node.prev_node = prev_node
        node.next_node = None
        node.prev_node = None
    
    def _move_to_front(self, node):
        curr_head = self.head.next_node
        curr_head.prev_node = node
        node.next_node = curr_head
        node.prev_node = self.head
        self.head.next_node = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove_node(node)
        self._move_to_front(node)
        return self.map[key].val
        

    def put(self, key: int, value: int) -> None:
        curr_head = self.head.next_node
        curr_head.prev_node = node
        node.next_node = curr_head
        node.prev_node = self.head
        self.head.next_node = node

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove_node(node)
            self._move_to_front(node)
            return

        node = ListNode(val=value, key=key)

        self._move_to_front(node)
        self.map[key] = node

        while len(self.map) > self.capacity:
            lru = self.tail.prev_node
            self._remove_node(lru)
            del self.map[lru.key]
