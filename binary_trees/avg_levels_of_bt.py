from collections import deque

def sol(root):
    lst_avg = []
    if not root:
        return lst_avg
    
    if root:
        lst_avg.append(root.val)

    q = deque([root])

    while q:
        curr_sum = 0
        nodes = 0

        for _ in range(len(q)):
            curr_node = q.popleft()

            if not curr_node:
                continue

            right = curr_node.right
            left = curr_node.left

            if right:
                curr_sum += right.val
                nodes += 1
                q.append(right)
            
            if left:
                curr_sum += left.val
                nodes += 1
                q.append(left)
        
        if nodes:
            lst_avg.append(curr_sum / nodes)
    return lst_avg