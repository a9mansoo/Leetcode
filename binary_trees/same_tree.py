from collections import deque


def isSameTree(p, q):
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def sol(p, q):
    p_queue = deque([p.left, p.right])
    q_queue = deque([q.left, q.right])
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    
    while p_queue and q_queue:
        p_left = p_queue.popleft()
        p_right = p_queue.popleft()
        q_left = q_queue.popleft()
        q_right = q_queue.popleft()

        
        if not p_left and q_left or not q_left and p_left:
            return False
        
        if not q_right and p_right or not p_right and q_right:
            return False
        
        if p_left is None and q_left is not None:
            return False
        
        if p_right is None and q_right is not None:
            return False
        
        if q_left is None and p_left is not None:
            return False
        
        if q_right is None and p_right is not None:
            return False

        if p_left and q_left and p_left.val != q_left.val:
            return False
        
        if p_right and q_right and p_right.val != q_right.val:
            return False
        
        if p_left:
            p_queue.append(p_left.left)
            p_queue.append(p_left.right)
        if q_left:
            q_queue.append(q_left.left)
            q_queue.append(q_left.right)

        if p_right:
            p_queue.append(p_right.left)
            p_queue.append(p_right.right)
        if q_right:
            q_queue.append(q_right.left)
            q_queue.append(q_right.right)
    return True