#Stack Implementation using deque modules

from queue import LifoQueue

stack = LifoQueue(maxsize = 3)
print(stack.qsize())

stack.put('a')
stack.put('b')
print(stack.qsize())
print(stack.full())
print(stack.get())