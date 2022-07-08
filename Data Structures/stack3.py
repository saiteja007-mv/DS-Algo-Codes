class Stack:
    def __init__(self):
        self.stack = []
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            print(dataval," Successfully inserted into stack")
        else:
            return False
    def remove(self):
        if len(self.stack) <= 0:
            print("No element is present in stack")
        else:
            print(self.stack.pop())
    def __str__(self):
        print(str(self.stack))
    
values = Stack()
values.add("teja")
values.add("sai")
values.add("bunny")
values.__str__()
values.remove()
values.__str__()