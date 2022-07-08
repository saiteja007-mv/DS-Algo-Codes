#Queue implementation using queue modules

from queue import Queue

queue = Queue(maxsize = 3)

queue.put(2)
queue.put(3)
queue.put(4)

queue.full()
queue.qsize()

queue.get()
queue.get()