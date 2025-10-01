


class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0
    
    def append(self, item):
        self.stack.append(item)
        self.size += 1
    
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()
        return -1
    
    def top(self):
        if self.size > 0:
            return self.stack[-1]
        return -1
    
    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def show_stack(self):
        for item in self.stack:
            print("-----------------")
            print(f"{item}")
            print("------------------")


lst_elems = [1, 4, 6, 3, 2, 7]
stack = Stack()
results = [-1]*len(lst_elems)

for i in range(len(lst_elems)):

    while not stack.is_empty() and lst_elems[i] > lst_elems[stack.top()]:
        results[stack.pop()] = lst_elems[i]
        stack.show_stack()
    
    stack.append(i)
    stack.show_stack()

print(results)