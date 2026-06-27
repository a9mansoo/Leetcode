from collections import deque
from build_tree import build_tree


def isMirror(left, right):
    if not left and not right:
        return True
    elif not left or not right:
        return False
    else:
        return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)

def sol_1(root):
    if not root:
        return True
    return isMirror(root.left, root.right)


def sol_2(root):
    q = deque([root.left, root.right])

    while q:
        left = q.popleft()
        right = q.popleft()

        if not left or not right:
            return False
        
        if not left and not right:
            continue

        if left.val != right.val:
            return False
        
        q.append(left.left)
        q.append(right.right)
        q.append(left.right)
        q.append(right.left)
    return True

root = build_tree([1,2,2,None,3,None,3])
print(sol_1(root))
print(sol_2(root))
