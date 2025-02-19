## 선형 큐 동작 원리 ##
# 인덱스로 실행이 되기 때문에 속도가 빠르다. ==> BFS, 다이스트라, 위상정렬
# 하지만, 코드가 조금 복잡해질 수 있다.
# 사이즈가 크면 큐를 사용하면 속도가 빠르다.
# 스택과는 용도가 다른 것!

# 큐 생성
queue = [0] * 3
front = rear = -1

# 1, 2, 3 인큐
rear += 1
queue[rear] = 1    # enqueue 1

rear += 1
queue[rear] = 2    # enqueue 2

rear += 1
queue[rear] = 3    # enqueue 3

# # 1. 꺼내기 ==> 꺼내도 되는지 확인을 해주고 꺼내는 것이 맞긴하다.
# front += 1
# print(queue[front])    # dequeue
#
# front += 1
# print(queue[front])    # dequeue
#
# front += 1
# print(queue[front])    # dequeue

# 2. 꺼내도 되는지 확인하는 방법
while rear != front:    # 큐에 원소가 남아있으면
    front += 1
    t = queue[front]
    print(t)


# 3. pop을 이용해 인큐, 디큐 구현하기
q = []
q.append(1)    # enqueue 1
q.append(2)
q.append(3)

print(q.pop(0))    # dequeue
print(q.pop(0))
print(q.pop(0))