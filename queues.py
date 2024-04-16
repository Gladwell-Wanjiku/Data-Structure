
#using a double ended queue
from collections import deque
q=deque()
q.append(7)
q.append(17)
q.append(22)
q.append(77)
print(q)
print(q.popleft())

#
from queue import Queue
m = Queue(maxsize=3)
print(m.qsize())
m.put('Gladwell')
m.put('wanjiku')
m.put('Njoroge')

print(m.full())
print(m.get())
print(m.get())
print(m.get())
print(m.empty())
print(m.full())