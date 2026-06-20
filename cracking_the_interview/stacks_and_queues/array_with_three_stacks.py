

class ThreeStack:


    def __init__(self):
        self.array = []
        self.stack_tops = [0] * 3
        self.arr_next = []
    

    def push(self, stack_index, value):
        self.array.append(value)
        top_index = self.stack_tops[stack_index]
        self.arr_next.append(top_index)
        self.stack_tops[stack_index] = len(self.array) - 1

