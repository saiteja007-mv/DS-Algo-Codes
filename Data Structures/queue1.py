#Queue implementaion using collections deque

from collections import deque

queue = deque()

queue.append('a')
queue.append('b')
queue.append('c')

print(queue)

print(queue.popleft())

print(queue)