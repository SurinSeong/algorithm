# 일반 리스트 vs deque

from collections import deque

q = deque()
q.append(1)    # enqueue 1
t = q.popleft()    #  dequeue