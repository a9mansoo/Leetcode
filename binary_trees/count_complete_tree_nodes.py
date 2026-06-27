from collections import deque

def countCompleteTree(root):
    if not root:
            return 0
    q = deque([root])
    count = 1

    while q:
        curr_node = q.popleft()

        if not curr_node:
            continue

        if curr_node.left:
            count += 1
            q.append(curr_node.left)
        
        if curr_node.right:
            count += 1
            q.append(curr_node.right)
    return count