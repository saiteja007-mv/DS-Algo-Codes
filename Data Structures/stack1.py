#Stack implementation using collections.deque

from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)